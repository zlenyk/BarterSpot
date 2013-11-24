from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from BarterSpot.announcements.models import Announcement
from BarterSpot.users.models import BarterUser
from BarterSpot.users.forms import RegisterForm

def index(request):
    ann_list = Announcement.getAllAnnouncements()
    return render(request, 'index.html', {'announcement_list': ann_list})
	
def searchPanel(request):
    return render(request, 'searchPanel.html')

def search(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        result_list = BarterUser.getUserByNames(first_name,last_name)
        if(len(result_list) == 0):
            result_list = BarterUser.getUserByLastName(last_name)
        
        return render(request, 'searchResult.html', {'result_list': result_list})
    else:
        return HttpResponseRedirect('/')

def searchAnnouncements(request):
    if request.method == 'POST':
        words = request.POST['topic']
        words_list = words.split()
        announcement_list = []
        for word in words_list:
            announcement_list += Announcement.getAnnouncementsWithTag(word)

        return render(request,'searchAnnouncementsResult.html', {'result_list':announcement_list})

    else:
        return HttpResponseRedirect('/')
