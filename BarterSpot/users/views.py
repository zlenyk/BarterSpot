# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render
from models import Member
def register_view(request):
    return render(request, 'users/register.html', None)

def add_user(request):
    uname = request.POST.get('username')
    passw = request.POST.get('password')
    email = request.POST.get('email')
    User.objects.create_user(uname,email,passw)
    
    firstName = request.POST.get('first_name')
    lastName = request.POST.get('last_name')
    _city = request.POST.get('city')
    member = Member(username=uname,first_name=firstName, last_name=lastName,city=_city)
    member.save()
    return render(request,'base.html', None)

def login_view(request):
    return render(request, 'users/login.html', None)

def auth_user(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        context = None
    	return render(request, 'base.html', context)
    else:
        # Show an error page
        context = None 
    	return render(request, 'base.html', context)
