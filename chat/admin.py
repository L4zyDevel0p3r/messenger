from django.contrib import admin
from .models import Message


# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("__str__", "group", "date")

    class Meta:
        model = Message
