from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=50)

class Language(models.Model):
    name = models.CharField(max_length=50)

class Cityis(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
