from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Profile(AbstractUser):
  image = models.ImageField(blank=True, null=True, upload_to='profile/')
  followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)