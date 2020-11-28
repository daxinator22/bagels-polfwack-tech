from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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




class Ingredients(models.Model):
    type = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inv_count = models.IntegerField(default=0)
    def __str__(self):
        return self.type


class BagelSandwich(models.Model):
    ingredients = []


class Order(models.Model):
    items = models.CharField(max_length=200, default='none')
    isMade = models.BooleanField(default=False)
    isFilled = models.BooleanField(default=False)

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
