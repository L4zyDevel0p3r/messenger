from django.contrib.auth.models import AbstractUser
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


# Create your models here.

class User(AbstractUser):
    pass
