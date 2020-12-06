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


from .models import foodItem, Order, Ingredients, BagelSandwich
from django.contrib.auth.models import Group

from django.urls import reverse_lazy
from django.views import generic
from django import forms
from .forms import SignUpForm, CheckForm, addMoneyForm, FoodItemForm, IngredientsForm
from django.contrib import messages

def get_user_context(request):
    urls = {}
    group = None
    button_link = '/accounts/login/'
    try:
        group = str(request.user.groups.all()[0])
    except IndexError:
        group = "No Group"

    if group == "Customer":
        urls.update({
            "Build Your Bagel!": "/build/",
            'Add Money': '/addMoney/',
        })
        button_link = '/build/'

    elif group == "Cashier":
        urls.update({
            "Check Queue": "/queue/",
        })
        button_link = '/queue/'

    elif group == "Chef":
        urls.update({
            "Check Queue": "/queue/",
        })
        button_link = '/queue/'

    elif group == "Manager":
        urls.update({
            "Check Queue": "/queue/",
            "Inventory": "/inventory/",
            "Create User": "/signup/",
        })
        button_link = '/inventory/'

    context = {
            'user': request.user,
            'group': group,
            'urls': urls,
            'button_link': button_link,
    }
    return context

def index(request):
    context = get_user_context(request)
    #return HttpResponse(template.render(context, request))
    return render(request, 'home/index.html', context)

def confirmation(request):
    context = get_user_context(request)
    return render(request, 'home/confirmation.html', context)

def build(request):
    #template = loader.get_template('home/orderBuild.html')
    print("Processing Order: ", request.method)
    food_list = foodItem.objects.order_by('-price')
    ingredient_list = Ingredients.objects.all()

    context = {
        'food_list': food_list,
        'ingredient_list': ingredient_list
    }
    context.update(get_user_context(request))
    if request.method == 'POST':
        form = CheckForm(request.POST)

        if form.is_valid():
            checked = request.POST.getlist('checked')
            ingrChecked = request.POST.getlist('ingrChecked')
            bagelCheck = request.POST.getlist('bagelCheck')
            order = request.user.profile.order
            for item in checked:
                currFoodItem = foodItem.objects.get(item_id=item)
                print("CurrFoodItem: ", currFoodItem.type)
                order.bagels.append(currFoodItem)



            sandwich = BagelSandwich.objects.create()
            sandwich.clearIng()

            for x in bagelCheck:
                sandwich.setBagel(x)
                break

            ingrs = []

            for item in ingrChecked:
                currIngr = Ingredients.objects.get(type=item)
                ingrs.append(currIngr)

            sandwich.setIngredients(ingrs)
            order.sandwiches.append(sandwich)
            print(order.bagels)


        return redirect('/build')
    else:
        return render(request, 'home/build.html', context)

def clearOrder(request):
    user = request.user
    user.profile.order.bagels.clear()
    user.profile.order.sandwiches.clear()
    user.save()
    return redirect('/home/build/checkout')

def checkout(request):
    user = request.user
    order_list = user.profile.order.bagels
    sandwich_list = user.profile.order.sandwiches
    total_price = 0
    for item in order_list:
        total_price += item.price
    for sandwich in sandwich_list:
        total_price += sandwich.getBagelPrice()
        for item in sandwich.ingredients:
            total_price += item.price


    context = {
        'order_list': order_list,
        'total_price': total_price,
        'sandwich_list': sandwich_list,

    }
    context.update(get_user_context(request))
    if request.method == 'POST':
        items = ''
        if user.profile.currency > total_price:
            for item in order_list:
                item.remove_from_inv(1)
                item.save()
                items = items + f'{str(item.id)},'
            for sandwich in sandwich_list:
                for item in sandwich.ingredients:
                    item.remove_from_inv(1)
                    item.save()
                    items = items + f'{str(item.id)},'

            o = Order(items=items)
            if request.POST.get('pickUpTime'):
                date = request.POST.get('pickUpTime')
                o.pickUpTime = date

            o.save()
            order_list.clear()
            sandwich_list.clear()
            total_price = 0
            user.profile.currency = user.profile.currency - total_price
            user.profile.order.bagels.clear()
            user.profile.order.sandwiches.clear()
            user.save()
            return render(request, 'home/confirmation.html', context)

    return render(request, 'home/checkout.html', context)

def queue(request):
    user_context = get_user_context(request)
    order_list = Order.objects.all()
    context = {
        'user': request.user,
        'order_list': order_list,
    }
    context.update(user_context)
    return render(request, 'home/queue.html', context)

def fill_order(request, order_id):
    user_context = get_user_context(request)
    item_string = Order.objects.filter(id=int(order_id))[0].items
    item_list = item_string.split(',')
    item_obj = list()
    for item in item_list:
        if item != '':
            item_obj.append(foodItem.objects.filter(id=item)[0])

    context = {
        'order': get_object_or_404(Order, pk=order_id),
        'items': item_obj,
    }
    context.update(user_context)
    return render(request, 'home/fill_order.html', context)

def isMade(request, order_id):
    order = Order.objects.filter(id=order_id)[0]
    if order.isFilled:
        order.delete()
        return redirect('/queue')
    else:
        order.isMade = True
        order.save()
        return redirect(f'/fill_order/{ order_id }')

def isFilled(request, order_id):
    order = Order.objects.filter(id=order_id)[0]
    if order.isMade:
        order.delete()
        return redirect('/queue')
    
    else:
        order.isFilled = True
        order.save()
        return redirect(f'/fill_order/{ order_id }')

def inventory(request):
    bagel_list = foodItem.objects.exclude(
        type__in = ['Sandwich', 'Shmear', 'Drink'],

    )
    shmear_list = foodItem.objects.exclude(
        type__in = ['Sandwich', 'Drink', 'Bagel'],
    )
    drink_list = foodItem.objects.exclude(
        type__in = ['Sandwich', 'Bagel', 'Shmear'],
    )
    ing_list = Ingredients.objects.all()
    context = {
        'bagel_list' : bagel_list,
        'shmear_list' : shmear_list,
        'drink_list' : drink_list,
        'ing_list' : ing_list,
    }
    context.update(get_user_context(request))
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        print('VALID: ', form.is_valid())
        if form.is_valid():
            item = request.POST.get('item')
            type = request.POST.get('type')
            amount = request.POST.get('amount')
            amount = int(amount)
            food = foodItem.objects.get(type=type, sub_type=item)
            food.add_to_inv(amount)
            food.save()
            foodItem.objects.update()
        else:
            form = IngredientsForm(request.POST)
            if form.is_valid():
                type = request.POST.get('type')
                amount = request.POST.get('amount')
                amount = int(amount)
                food = Ingredients.objects.get(type=type)
                food.add_to_inv(amount)
                food.save()
                Ingredients.objects.update()


    return render(request, 'home/inventory.html', context)

def addMoney(request):
    user = request.user
    context = get_user_context(request)
    if request.method == 'POST':
        form = addMoneyForm(request.POST)
        print("Errors: ", form.errors)
        print("Valid: ", form.is_valid())
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            user.profile.currency = user.profile.currency + amount
            user.save()




    return render(request, 'home/addMoney.html', context)



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
