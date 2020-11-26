from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('build/', views.build, name='build'),
    path('build/checkout/', views.checkout, name='checkout'),
    url('signup/', views.signup, name='signup'),
    path('queue/', views.queue, name='queue'),
    path('fill_order/', views.fill_order, name='fill_order'),
    path('inventory/', views.inventory, name='inventory'),
    path('addMoney/', views.addMoney, name='addMoney'),

]
