from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

TYPES = (
    ('TOURIST', 'Tourist'),
    ('BUSINESS', 'Business'),
    ('STUDENT', 'Student'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    user_type = models.CharField(max_length=15, choices=TYPES)

class Data(models.Model):
    author = models.ForeignKey('auth.User', default="none")
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    long_description = models.TextField()
    data_type = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    link = models.CharField(max_length=500)
    map_link = models.TextField()
    image_link = models.TextField()

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
