from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers

from .models import Item, Order

def signup(request):
	return render(request, 'members/signup.html', {})

def register(request):
	user = User.objects.create_user(username = request.POST["username"], email = request.POST["email"])
	user.set_password(request.POST["password"])
	user.save()
	return render(request, 'members/members.html', {})

def authenticate_user(request):
    return render(request, 'members/login_user.html', {})

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user:
        if user.is_active:
            login(request, user)
            render(request, 'members/members.html', {})
    else:
        return render(request, 'members/signup.html', {})

def logout_view(request):
    logout(request)

def showall(request):
    item_list = Item.objects.all()
    if item_list == request.GET.get('format'):
        data=serializers.serialize("json", Item.objects.all())
        return HttpResponse(data, content_type='application/json') 
    else:
        return render(request, 'members/showall.html', {'items':item_list})

def showlatest(request):
    return render(request, 'members/showlatest.html', {'item':Item.objects.all()[0]})

def showone(request):
    name = request.GET.get("name", '')
    item = Item.objects.filter(name=name)
    if item:
        return render(request, 'members/showlatest.html', {'item':name})
    else:
        return HttpResponse('Nothing here!')

def listing(request):
    item_list = Item.objects.all()
    paginator = Paginator(item_list, 5)


    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    return render(request, 'members/listing.html', {"items":items, "page":page})

def add(request, item_id):
    item = Item.objects.filter(id=item_id)
    #check if authenticated user
        #check if orders
            #if none, then create order
            #if orders, check status=1
                #add items to order
            #if no order=1, create order
    #else redirect to signup

        #add item to cart
        #redirect to cart
    #else
        #redirect to login page


