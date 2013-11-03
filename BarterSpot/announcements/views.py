# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response


def index(request):
	context = None
	return render(request, 'base.html', context)

def add_page(request):
	return render(request, 'announcements/add.html', None)

def add_announcement(request):
        _member = request.POST.get('member','')
	_title = request.POST.get('title','')
	_pub_date = request.POST.get('pub_date','')
	announcement = Announcement(
	    member = _member,
	    title = _title,
	    pub_date = _pub_date
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
        
        context = None
	return render(request, 'base.html', context)
