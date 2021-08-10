from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils.html import conditional_escape
from channels.db import database_sync_to_async
from messenger.settings import STATIC_URL
from group.models import Group
from .models import Message
import json


class ChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def check_group(self):
        qs = Group.objects.filter(url_name__iexact=self.room_name, active=True)
        if qs.exists():
            return qs.first()
        else:
            return None

    @database_sync_to_async
    def db_create_message(self, message):
        group = Group.objects.get_by_url_name(self.room_name)
        encrypted_message = Message.encrypt_text(message)
        return Message.objects.create(author_id=self.user.id, group_id=group.id, text=encrypted_message)

    @database_sync_to_async
    def get_msg_author_username(self, msg):
        return msg.author.username

    async def connect(self):
        self.user = self.scope.get("user")

        if self.user.is_authenticated:
            # room_name lower mishe chon age lower nashe user to room dg i vali ba name i shabih room_name add mishe.
            # masalan room 'lobby' ba 'LoBbY' nabayad farghi kone ama chon horof bozorg va kochik daran dar bakhsh
            # 'self.channel_layer.group_add' group haye joda i hesab mishan.
            # pas lower case mishe ta in etefagh nayofte
            self.room_name = (self.scope.get("url_route").get("kwargs").get("room_name")).lower()

            group_qs = await self.check_group()

            if group_qs is not None:
                self.room_group_name = f"chat_{self.room_name}"

                await self.channel_layer.group_add(self.room_group_name, self.channel_name)
                await self.accept()

                username = self.user.username
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        "type": "send_message",
                        "message": f"'{username}' joined the room.",
                        "author": "SERVER",
                        "author_pic": STATIC_URL + "img/Bot.png"
                    }
                )

            # There is no group named room_name in the database
            else:
                await self.close()

        # User is not authenticated
        else:
            await self.close()

    async def disconnect(self, code):
        username = self.user.username
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "send_message",
                "message": f"'{username}' left the room.",
                "author": "SERVER",
                "author_pic": STATIC_URL + "img/Bot.png"
            }
        )

        for group in self.groups:
            await self.channel_layer.group_discard(group, self.channel_name)

    async def receive(self, text_data):
        data: dict = json.loads(text_data)
        message = data.get("message")

        msg = await self.db_create_message(message=message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "send_message",
                "message": conditional_escape(message),
                "author": await self.get_msg_author_username(msg),
                "author_pic": msg.author.picture.url
            }
        )

    async def send_message(self, event):
        message = event.get("message")
        author = event.get("author")
        author_pic = event.get("author_pic")

        await self.send(text_data=json.dumps({
            "message": message,
            "author": author,
            "author_pic": author_pic
        }))
