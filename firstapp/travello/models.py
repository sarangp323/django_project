from django.db import models

# Create your models here.
class Destination(models.Model):
    name : models.CharField(max_length=100)
    price : models.IntegerField()
    desc : models.CharField(max_length=100)
    offer: models.BooleanField(default=False)