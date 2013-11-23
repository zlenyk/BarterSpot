from django.conf.urls import patterns, url

from BarterSpot.messages import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^send/', views.send),
    url(r'^message=(?P<msg_id>\w+)/$', views.show_message),
)
