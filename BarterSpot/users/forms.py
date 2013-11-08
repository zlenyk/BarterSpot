from django import forms
from django.contrib.auth.forms import UserCreationForm
from BarterSpot.users.models import Member

class RegisterForm(UserCreationForm):
    username =  forms.CharField(max_length=100,required=True)
    first_name = forms.CharField(max_length=100,required=True)
    last_name = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(max_length=100,required=True)
    city = forms.CharField(max_length=100,required=True)
