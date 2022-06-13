from django.db import models
from django.contrib.auth.models import User
class Book(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    author=models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)
class BRMuser(models.Model):
    user=models.OneToOneField(User,on_delete='models.CASCADE')
    nickName=models.CharField(max_length=20,null=False)
