from django.db import models

# Create your models here.
class Getdata(models.Model):
    name = models.CharField(max_length=20)
    tel = models.TextField()