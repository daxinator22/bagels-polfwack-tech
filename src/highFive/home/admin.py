from django.contrib import admin
from .models import foodItem, Ingredients, Order

admin.site.register(foodItem)
admin.site.register(Ingredients)
admin.site.register(Order)

# Register your models here.
