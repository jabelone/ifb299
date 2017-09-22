from django.db import models
from django.utils import timezone

class Login(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    user_type = models.CharField(max_length=30)

    def __str__(self):
        return self.name+' - '+self.type


class Data(models.Model):
    author = models.ForeignKey('auth.User', default="none")
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=100)
    long_descriptiion = models.TextField()
    data_type = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=10)
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
