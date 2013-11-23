from django import forms
from BarterSpot.messages.models import Message
from django.forms import ModelForm

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body']
