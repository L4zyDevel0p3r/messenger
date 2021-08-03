from django.utils.translation import gettext_lazy as _
from cryptography.fernet import Fernet
from account.models import User
from group.models import Group
from django.db import models

# SECURITY WARNING: keep the encryption key secret!
ENCRYPTION_KEY = b'f5cQj1_Pv68Qe-iNh1oml03pRZR4LIJllS8qFpJtTzg='


# Create your models here.


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("author"))
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name=_("group"))
    text = models.TextField(verbose_name=_("text"))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_("date"))

    @staticmethod
    def encrypt_text(text: str) -> str:
        # Converting 'text' to bytes
        text = text.encode()
        # Creating Fernet object
        f = Fernet(ENCRYPTION_KEY)
        # Encrypting 'text', converting it from bytes to string and returning it
        return (f.encrypt(text)).decode()

    @staticmethod
    def decrypt_text(text: str) -> str:
        # Converting 'text' to bytes
        text = text.encode()
        # Creating Fernet object
        f = Fernet(ENCRYPTION_KEY)
        # Decrypting 'text', converting it from bytes to string and returning it
        return (f.decrypt(text)).decode()

    class Meta:
        verbose_name_plural = _("messages")
        verbose_name = _("message")

    def __str__(self):
        return self.author.username
