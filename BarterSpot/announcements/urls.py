from django.conf.urls import patterns, url

from BarterSpot.announcements import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
