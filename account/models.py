from django.contrib.auth.models import AbstractUser
from django.db import models
import os


def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)
    return name, ext


# Create your models here.

class User(AbstractUser):
    pass
