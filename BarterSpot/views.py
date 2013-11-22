from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from BarterSpot.announcements.models import Announcement
from BarterSpot.users.models import BarterUser
from BarterSpot.users.forms import RegisterForm
from BarterSpot.announcements.models import Announcement
def index(request):
    ann_list = Announcement.getAllAnnouncements()
    return render(request, 'index.html', {'announcement_list': ann_list})

def searchUser(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        result_list = BarterUser.getUserByNames(first_name,last_name)
        if(len(result_list) == 0):
            result_list = BarterUser.getUserByLastName(last_name)
        
        return render(request, 'searchResult.html', {'result_list': result_list})
    else:
        return HttpResponseRedirect('/')

def searchAnnouncement(request):
    if request.method == 'POST':
        words = request.POST['topic']
        #city = request.POST['city']
        words_list = words.split()
        announcement_list = None
        for word in words_list:
            announcement_list += Announcement.getAnnouncementsWithTag(word)
        return render(request,'searchAnnouncementsResult.html', {result_list:announcement_list})

    else:
        return HttpResponseRedirect('/')
