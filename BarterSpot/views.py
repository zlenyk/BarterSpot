from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from BarterSpot.announcements.models import Announcement


def index(request):
    ann_list = Announcement.getAllAnnouncements()
    return render(request, 'index.html', {'announcement_list': ann_list})
