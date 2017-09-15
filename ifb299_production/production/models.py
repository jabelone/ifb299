from django.db import models

# Create your models here.


class User(models.Model):

    name = models.TextField()
    password = models.TextField()
    phone = models.TextField()
    email = models.EmailField()
    address = models.TextField()
    type = models.TextField()

    def __str__(self):
       return self.name