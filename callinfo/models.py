from django.db import models

# Create your models here.


class User(models.Model):
    # username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    phoneno = models.IntegerField(unique=True)
    spam = models.CharField(max_length=3, default='No', editable=False)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=50)


class GlobalUsers(models.Model):
    phoneno = models.IntegerField()
    name = models.CharField(max_length=30)
    spam = models.CharField(max_length=3, default='No', editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='globalusers', editable=False, null=True)