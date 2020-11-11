from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Bagel(models.Model):
    bagel_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.bagel_text

class Customer(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    emailAddress = models.CharField(max_length=200)
    def __str__(self):
        return self.name



