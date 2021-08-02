from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.db.utils import IntegrityError
from django.dispatch import receiver
from django.urls import reverse
from django.db import models


# Create your models here.


class GroupManager(models.Manager):
    def filter_by_active(self):
        qs = self.get_queryset().filter(active=True)
        return qs

    def get_by_name(self, name):
        qs = self.get_queryset().filter(name__iexact=name)

        if qs.exists():
            return qs.first()
        else:
            return None

    def get_by_url_name(self, url_name):
        qs = self.get_queryset().filter(url_name__iexact=url_name)

        if qs.exists():
            return qs.first()
        else:
            return None


class Group(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name=_("name"))
    url_name = models.CharField(max_length=20, unique=True, verbose_name=_("url name"))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_("date"))
    active = models.BooleanField(default=False, verbose_name=_("active"))

    objects = GroupManager()

    def get_absolute_url(self):
        return reverse("ChatApp:RoomPage", kwargs={"room_name": self.url_name})

    class Meta:
        verbose_name_plural = _("groups")
        verbose_name = _("group")

    def __str__(self):
        return self.name


@receiver(sender=Group, signal=pre_save)
def group_pre_save_receiver(sender, instance, *args, **kwargs):
    qs1 = sender.objects.get_by_name(instance.name)
    if qs1 is not None and qs1 != instance:
        raise IntegrityError(_("A group with that name already exists."))

    qs2 = sender.objects.get_by_url_name(instance.url_name)
    if qs2 is not None and qs2 != instance:
        raise IntegrityError(_("A group with that url name already exists."))
