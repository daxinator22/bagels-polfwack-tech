from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import foodItem

from django.urls import reverse_lazy
from django.views import generic


def index(request):

    context = {

    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'home/index.html', context)

def build(request):
    #template = loader.get_template('home/orderBuild.html')
    food_list = foodItem.objects.order_by('-price')
    context = {
        'food_list': food_list,
    }
    return render(request, 'home/build.html', context)

def checkout(request):
    context = {

    }
    return render(request, 'home/checkout.html', context)

def login(request):
    context = {

    }
    return render(request, 'home/login.html', context)

# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'
