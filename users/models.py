from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''class Bbs_user(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=128, default='这个家伙很懒，什么都没留下')
    #photo = models.ImageField(upload_to='upload_imgs/', defaule='upload_imgs/user_1.jpg')
    #name = models.CharField(max_length=32, default=1)
    name = models.CharField(max_length=16)
    def __str__(self):
        return self.user.username

'''