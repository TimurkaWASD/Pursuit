from django.db import models
from django_countries.fields import CountryField

class Country(models.Model):
    name = CountryField()

class Language(models.Model):
    name = models.CharField(max_length=50)


