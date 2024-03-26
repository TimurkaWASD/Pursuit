from django.db import models

class Target(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.IntegerField(default=0)
    image = models.ImageField(upload_to='')
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField()
    status = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)