# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render
from models import BarterUser, Validation
from BarterSpot.users.forms import RegisterForm, EditForm
from BarterSpot.announcements.models import Announcement
from django.core.context_processors import csrf
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.http import HttpResponseRedirect
from BarterSpot.utils.utils import generateRandomString, sendValidationMail


def register_user(request):
    if request.user.is_authenticated():
        return render(request, 'users/register', {'has_account': True})

    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        validate = request.POST.get('validate', '')
        if user_form.is_valid():
            _username = user_form.cleaned_data['username']
            _first_name = user_form.cleaned_data['first_name']
            _last_name = user_form.cleaned_data['last_name']
            _email = user_form.cleaned_data['email']
            _password = user_form.cleaned_data['password1']
            _city = user_form.cleaned_data['city']
            if validate:
                newUser = BarterUser.createUser(username=_username,
                                                email=_email,
                                                first_name=_first_name,
                                                last_name=_last_name,
                                                password=_password,
                                                city=_city)
                strHash = generateRandomString()
                Validation.createValidation(newUser, strHash)
                sendValidationMail(_username, _email, strHash)
            else:
                BarterUser.createUser(username=_username,
                                      email=_email,
                                      first_name=_first_name,
                                      last_name=_last_name,
                                      password=_password,
                                      city=_city,
                                      validate=False)
            return HttpResponseRedirect('/')
        else:
            c = {'valid': False, 'form': user_form}
            _username = request.POST['username']
            if BarterUser.userWithLoginExists(_username):
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


def show_profile(request, _username):
    _user = BarterUser.getUserByLogin(_username)
    if _user is not None:
        ann_list = _user.getAnnouncements()
        return render(request, "users/profile.html", {'barter_user': _user, 'ann_list': ann_list})
    else:
        return render(request, "errorPage.html",
                      {'message': "User " + _username + " does not exist"})
		

def validate(request, strHash):
    val = Validation.getValidation(strHash)
    if val is not None:
        Validation.validate(val)
        return render(request, "simple_message.html",
                      {'message': "Validation correct"})
    else:
        return render(request, "simple_message.html",
                      {'message': "Validation failed"})

def change(request, _username):
    if request.user.is_authenticated() == False:
        return render(request, 'users/edit.html', {'has_account': False})
    _user = BarterUser.getUserByLogin(_username)
    if request.method == 'POST':	
        user_form = SetPasswordForm(_user, request.POST)
	
        #_password1 = user_form.cleaned_data['new_password1']
	#_password2 = user_form.cleaned_data['new_password2']
	if user_form.is_valid():
	    user_form.save()
	    return render(request, "simple_message.html",
                      {'message': "Validation correct"})
	else:
	    return render(request, "simple_message.html",
                      {'message': "User form is invalid"})
    else:
	user_form = SetPasswordForm(_user)
	return render(request, 'users/change.html', {'form': user_form})

def edit(request, _username):
    if request.user.is_authenticated() == False:
        return render(request, 'users/edit.html', {'has_account': False})
    _user = BarterUser.getUserByLogin(_username)
    if request.method == 'POST':
        user_form = EditForm(request.POST)
        validate = request.POST.get('validate', '')
        _first_name = user_form.data['first_name']
        _last_name = user_form.data['last_name']
        _email = user_form.data['email']
        _city = user_form.data['city']
	_user.updateUserData(_first_name, _last_name, _email, _city)
	return render(request, "simple_message.html",
                      {'message': "Data changed!"})
    else:
	user_form = EditForm(request.POST)
	user_form.data['first_name'] = _user.first_name
	user_form.data['last_name'] = _user.last_name
	user_form.data['email'] = _user.email
	user_form.data['city'] = _user.city
	return render(request, 'users/edit.html', {'form': user_form})
