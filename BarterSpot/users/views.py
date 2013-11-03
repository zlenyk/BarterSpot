# Create your views here.

from django.contrib import auth
from django.shortcuts import render

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
