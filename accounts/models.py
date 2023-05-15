from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.conf import settings


# Create your models here.
class Profile(AbstractUser):
  nickname = models.CharField(max_length=10)
  photo = models.ImageField(blank=True, upload_to='profile/')
  # def get_absolute_url(self):
  #   return reverse('posts:index')