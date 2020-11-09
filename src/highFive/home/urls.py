from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('build/', views.build, name='build'),
    path('build/checkout/', views.checkout, name='checkout'),
    path('logIn/', views.logIn, name='logIn'),
]