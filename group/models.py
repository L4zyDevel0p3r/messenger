from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name=_("name"))
    url_name = models.CharField(max_length=20, unique=True, verbose_name=_("url name"))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_("date"))

    class Meta:
        verbose_name_plural = _("groups")
        verbose_name = _("group")

    def __str__(self):
        return self.name
