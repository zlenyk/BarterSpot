from django.conf.urls import patterns, url

from BarterSpot.announcements import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_announcement/', views.add_announcement, name ='add_announcement'),
    url(r'^add/', views.add_page, name='add_page')
)
