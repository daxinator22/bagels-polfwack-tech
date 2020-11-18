from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template

from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm as SignUpForm
# Create your views here.
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import SignUpForm
from .models import foodItem
from django.contrib.auth.models import Group

from django.urls import reverse_lazy
from django.views import generic
from django import forms


def index(request):
    context = {
            'user': request.user,
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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            group = Group.objects.get(name=request.POST.get('group'))
            user = authenticate(username=username, password=raw_password)
            user.groups.add(group)
            login(request, user)
            return redirect('/home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
