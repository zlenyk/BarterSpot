from django.conf.urls import patterns, url
from BarterSpot.users import views

urlpatterns = patterns('',
	url(r'^login/', views.login_user),
	url(r'^register/', views.register_user),
	url(r'^add/', views.register_user),
	url(r'^logout/', views.logout_user),
	url(r'^(?P<_username>\w+)/$', views.show_profile),
)

