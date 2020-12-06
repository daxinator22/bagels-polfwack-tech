from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('build/', views.build, name='build'),
    path('build/checkout/', views.checkout, name='checkout'),
    path('build/checkout/confirmation', views.confirmation, name='confirmation'),
    path('clearOrder', views.clearOrder, name='clearOrder'),
    url('signup/', views.signup, name='signup'),
    path('queue/', views.queue, name='queue'),
    path('fill_order/<order_id>/', views.fill_order, name='fill_order'),
    path('fill_order/<order_id>/isMade/', views.isMade, name='isMade'),
    path('fill_order/<order_id>/isFilled/', views.isFilled, name='isFilled'),
    path('inventory/', views.inventory, name='inventory'),
    path('addMoney/', views.addMoney, name='addMoney'),


]
