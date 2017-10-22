from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

<<<<<<< HEAD
=======

>>>>>>> master
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    user_type = models.CharField(max_length=30)

<<<<<<< HEAD
=======



>>>>>>> master
class Data(models.Model):
    author = models.ForeignKey('auth.User', default="none")
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=100)
    long_descriptiion = models.TextField()
    data_type = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    created_date = models.DateTimeField(default=timezone.now)
    edited_date = models.DateTimeField(default=timezone.now)


    # This is for the type specific info like department(s), industry type etc
    def special_default():
        return {"data": "null"}
    special = models.TextField("", default=special_default)

    def edit(self):
        self.edited_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
