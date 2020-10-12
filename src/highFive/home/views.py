from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template


# Create your views here.
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    template = loader.get_template('home/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def build(request):
    #template = loader.get_template('home/orderBuild.html')
    context = {

    }
    return render(request, 'home/build.html', context)

def checkout(request):
    context = {

    }
    return render(request, 'home/checkout.html', context)

# Create your views here.
