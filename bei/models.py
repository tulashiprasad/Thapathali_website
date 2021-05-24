from django.db import models
from django.db.models import query
from django.db.models.fields import NullBooleanField

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    querry = models.CharField(max_length=200)


    def __str__(self):
        return self.name


# class Login(models.Model):
#     email = models.EmailField(max_length=29)
#     password = models.CharField(max_length=20)

#     def __str__(self):
#         return self.email

# class SignUp(models.Model):
    
#     name = models.CharField(max_length=50, null=True)
#     phone = models.IntegerField()
#     email = models.EmailField(max_length=20)
#     password = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name
    




