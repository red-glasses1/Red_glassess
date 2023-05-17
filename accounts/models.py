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

  # 단방향으로 관계를 설정.
  follower_set = models.ManyToManyField('self', blank=True, related_name='following_set', symmetrical=False)