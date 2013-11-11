# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render
from models import Member
from BarterSpot.users.forms import RegisterForm
from django.core.context_processors import csrf
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect


def register_user(request):
    if request.user.is_authenticated():
        return render(request, 'users/register', {'has_account': True})

    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            _username = user_form.cleaned_data['username']
            _first_name = user_form.cleaned_data['first_name']
            _last_name = user_form.cleaned_data['last_name']
            _email = user_form.cleaned_data['email']
            _password = user_form.cleaned_data['password1']
            _city = user_form.cleaned_data['city']
            User.objects.create_user(username=_username,
                                     email=_email,
                                     first_name=_first_name,
                                     last_name=_last_name,
                                     password=_password)

            member = Member(username=_username, city=_city)
            member.save()
            return HttpResponseRedirect('/')
        else:
            c = {'valid': False, 'form': user_form}
            _username = request.POST['username']
            if _username is not None and \
                    User.objects.filter(username=_username).count() > 0:
                c['user_exists'] = True
            return render(request, 'users/register.html', c)
    else:
        user_form = RegisterForm()
        return render(request, 'users/register.html', {'form': user_form})


def login_user(request):
    if request.user.is_authenticated():
        return render(request, 'users/login.html', {'logged': True})

    login_form = AuthenticationForm()
    if request.method == 'POST':
        # retrieves fields from the Authentication Form
        _username = request.POST['username']
        _password = request.POST['password']
        user = auth.authenticate(username=_username, password=_password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            context = {'auth': True}
            return HttpResponseRedirect('/')
        else:
            # Show an error page
            context = {'auth': False, 'form': login_form}
            return render(request, 'users/login.html', context)
    else:
        return render(request, 'users/login.html', {'form': login_form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
