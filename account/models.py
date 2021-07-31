from django.contrib.auth.models import AbstractUser, UserManager
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from uuid import uuid4
import os


def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)
    return name, ext


def upload_user_pic(instance, file):
    name, ext = get_filename_ext(file)
    random_str = str(uuid4()).split("-")[0]
    final_name = f"profile_pictures/{instance.username}/{random_str}{ext}"
    return final_name


def validate_image_size(img):
    file_size = img.size
    limit_mb = 5

    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError(_(f"File size is larger than allowed ({limit_mb} mb)."))


# Create your models here.

class CustomUserManager(UserManager):
    def create_user(self, username, email=None, password=None, picture=None, **extra_fields):
        user = super().create_user(username=username, email=email, password=password, **extra_fields)
        user.picture = picture
        user.save()
        return user


class User(AbstractUser):
    picture = models.ImageField(
        upload_to=upload_user_pic, validators=[validate_image_size], null=True, verbose_name=_("Profile picture")
    )

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        try:
            this = User.objects.get(pk=self.pk)
            if this.picture != self.picture:
                this.picture.delete(save=False)
        except:
            pass  # When new photo then we do nothing, normal case

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = _('users')
        verbose_name = _('user')
        db_table = 'auth_user'
