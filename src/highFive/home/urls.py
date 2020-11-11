from django.urls import path
from . import views
# from .views import SignUpView


urlpatterns = [
    path('', views.index, name='index'),
    path('build/', views.build, name='build'),
    path('build/checkout/', views.checkout, name='checkout'),
    path('login/', views.login, name='login'),
    # path('signup/', SignUpView.as_view(), name='signup')
]
