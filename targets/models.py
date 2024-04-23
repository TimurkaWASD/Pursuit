from django.db import models
from user.models import CustomUser


class Target(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/targets', blank=True, null=True)
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField()
    status = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)