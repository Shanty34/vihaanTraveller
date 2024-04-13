from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    personality = models.CharField(max_length=30)
