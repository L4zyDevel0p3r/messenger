from django.utils.translation import gettext_lazy as _
from account.models import User
from group.models import Group
from django.db import models

ENCRYPTION_KEY = b'f5cQj1_Pv68Qe-iNh1oml03pRZR4LIJllS8qFpJtTzg='


# Create your models here.


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("author"))
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name=_("group"))
    text = models.TextField(verbose_name=_("text"))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_("date"))

    class Meta:
        verbose_name_plural = _("messages")
        verbose_name = _("message")

    def __str__(self):
        return self.author.username
