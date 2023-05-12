from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=80)
  image = models.ImageField(blank=False,upload_to='posters/')
  content = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
