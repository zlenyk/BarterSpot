# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from models import Announcement,Tag
from BarterSpot.users.models import Member


def index(request):
    context = None
    return render(request, 'index.html', context)


def add_page(request):
    return render(request, 'announcements/add.html', None)


def add_announcement(request):
    _member = Member.objects.get(username=request.user.username)
    _title = request.POST.get('title')
    _content = request.POST.get('content')
    announcement = Announcement(
        member=_member,
        title=_title,
        content=_content,
    )
    announcement.save()
    tagsStrList = request.POST.getlist('tag_list')
    # print("tag list size: " + str(len(tagsStrList)))
    # for strTag in tagsStrList:
    #     print(strTag + " " + str(type(strTag)))
    announcement.addTagsList(Tag.addTagsList(tagsStrList))
    announcement.save()
    return HttpResponseRedirect('/')
