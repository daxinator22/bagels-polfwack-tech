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
    funds = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    type = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    def __str__(self):
        return self.type


class BagelSandwich(models.Model):
    ingredients = []


class Order(models.Model):
    sandwiches = []
    bagels = []