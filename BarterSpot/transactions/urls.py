from django.conf.urls import patterns, url

from BarterSpot.transactions import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^make_transaction/(?P<want_id>\w+)/(?P<for_id>\w+)/$', views.make_transaction),
    url(r'^offer_exchange/(?P<want_id>\w+)/$', views.offer_exchange),
    url(r'^accept/(?P<tid>\w+)/$', views.accept),
    url(r'^reject/(?P<tid>\w+)/$', views.reject),
)
