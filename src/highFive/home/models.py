from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.utils import timezone
import random

# Create your models here.
class foodItem(models.Model):
    type = models.CharField(max_length=200)
    sub_type = models.CharField(max_length=200)
    inv_count = models.IntegerField(default=random.randint(1000, 140000))
    price = models.DecimalField(decimal_places=2,max_digits=10)
    #item_id = models.IntegerField()
    def __str__(self):
        return self.sub_type
    def addToInv(self, amount):
        self.inv_count += amount
    def removeFromInv(self, amount):
        self.inv_count -= amount





class Ingredients(models.Model):
    type = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inv_count = models.IntegerField(default=0)
    def __str__(self):
        return self.type
    def addToInv(self, amount):
        self.inv_count += amount
    def removeFromInv(self, amount):
        self.inv_count -= amount


class BagelSandwich(models.Model):
    ingredients = []
    def addItem(self, item):
        self.ingredients.append(item)


class Order(models.Model):
    items = models.CharField(max_length=200, default='none')
    isMade = models.BooleanField(default=False)
    isFilled = models.BooleanField(default=False)
    bagels = []
    sandwiches = []

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    order = Order()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
