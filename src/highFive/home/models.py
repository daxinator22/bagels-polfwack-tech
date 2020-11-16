from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class foodItem(models.Model):
    type = models.CharField(max_length=200)
    sub_type = models.CharField(max_length=200)
    inv_count = models.IntegerField()
    price = models.DecimalField(decimal_places=2,max_digits=10)
    def __str__(self):
        return self.sub_type

class Customer(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    emailAddress = models.CharField(max_length=200)
    def __str__(self):
        return self.name
