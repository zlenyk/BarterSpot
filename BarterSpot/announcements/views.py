# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from models import Announcement,Tag
from BarterSpot.users.models import BarterUser
from BarterSpot.images.models import BarterImage
# from BarterSpot.images.views import ImageUploadForm
from BarterSpot.utils.utils import authorizationCheck


def index(request):
    context = None
    return render(request, 'index.html', context)


@authorizationCheck
def add_page(request):
    return render(request, 'announcements/add.html', None)


@authorizationCheck
def add_announcement(request):
    print(request.POST.get("image", "ne ma :("))
    _user = BarterUser.getUserFromRequest(request)
    _title = request.POST.get('title')
    _content = request.POST.get('content')
    tagsStrList = request.POST.getlist('tag_list')
    tagsList = Tag.addTagsList(tagsStrList)
    newAnn = Announcement.createAnnouncement(_user, _title, _content, tagsList)
    if newAnn is not None:
        if request.FILES.get("image", ""):
            newImage = BarterImage.imageFromUpload(request.FILES["image"])
            print("upload successful")
            newAnn.setImage(newImage)
        # Should be "Announcement creation succcessful" or whatever
        return HttpResponseRedirect('/')
    else:
        # Should be "Announcement creation failed"
        return HttpResponseRedirect('/')


def show_announcement(request, ann_id):
    announcement = Announcement.getAnnouncementById(ann_id)
    if announcement is not None:
        return render(request, 'announcements/announcement.html', {'announcement': announcement})
    else:
        return render(request, "errorPage.html", {'message': "Announcement does not exist"})

def remove(request, ann_id):
    Announcement.removeAnnouncement(ann_id)
    return HttpResponseRedirect('/users/profile/'+request.user.username); 


