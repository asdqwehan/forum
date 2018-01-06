from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Bbs(models.Model):
    category = models.ForeignKey('Category')
    title = models.CharField(max_length=100)
    #summary = models.CharField(max_length=256,blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey(User)
    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    topic = models.ForeignKey(Bbs)
    content = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.content

class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    administrator = models.ForeignKey(User)

    def __str__(self):
        return self.name
