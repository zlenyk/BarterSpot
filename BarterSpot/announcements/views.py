# Create your views here.
from django.http import HttpResponse
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
	announcement = Announcement(
	    member = _member,
	    title = _title,
        )
	announcement.save()
	tag_list = request.POST.getlist('tag_list')
	tags = []
	for tag in tag_list:
	    temp_tag = Tag.objects.get(name=tag)
	    if temp_tag == None:
	        tags.add(Tag(name = tag))
	    else:
	        tags.add(temp_tag)
		temp_tag.count = temp_tag.count+1
        
	for tag in tags:
	    announcement.tags.add(tag)
	
	announcement_list = Announcement.objects.order_by('pub_date')

	return render(request,'index.html',{'announcement_list':announcement_list})
