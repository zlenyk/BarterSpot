# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def index(request):
	context = None
	return render(request, 'base.html', context)
