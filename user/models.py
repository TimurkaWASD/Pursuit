from django.contrib.auth.models import AbstractUser
from django.db import models
from additionallyuser.models import Language
from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    password = models.CharField(max_length=225)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='images/profile', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    languages = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)
    country = CountryField(blank=True, null=True)



    def __str__(self):
        return self.username
