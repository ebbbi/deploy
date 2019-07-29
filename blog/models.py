from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField(default=timezone.now)
    eyes=models.TextField(default='')
    lip=models.TextField(default='')
    face=models.TextField(default='')
    category=models.CharField(max_length=255, default='')
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content=models.TextField()
    time=models.DateTimeField(default=timezone.now)