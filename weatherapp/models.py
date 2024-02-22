from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Favorate(models.Model):
    cityname=models.CharField(max_length=255,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.cityname