from django.db import models
from django.conf import settings
import re

# Create your models here.
class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField(max_length=80)
  image = models.ImageField(blank=False,upload_to='posters/')
  content = models.CharField(max_length=500)
  Tag_set = models.ManyToManyField('Tag',blank=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.content

  def extract_tag_list(self):

    return re.findall(r"#([a-zA-Z\dㄱ-힣]+)", self.content)

class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return self.name
