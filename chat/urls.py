from django.urls import path
from .views import room_page

app_name = "ChatApp"

urlpatterns = [
    path("chat/<str:room_name>", room_page, name="RoomPage"),
]
