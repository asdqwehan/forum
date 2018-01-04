from django.db import models
from users.models import Bbs_user
# Create your models here.
class Bbs(models.Model):
    title = models.CharField(max_length=100)
    #summary = models.CharField(max_length=256,blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey(Bbs_user)
    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField()

    def __str__(self):
        return self.title

class Comments(models.Model):
    topic = models.ForeignKey(Bbs)
    content = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Bbs_user)

    def __str__(self):
        return self.content

class Catepory(models.Model):
    nama = models.CharField(max_length=32, unique=True)
    administrator = models.ForeignKey(Bbs_user)
