from django.conf.urls import patterns, url
from BarterSpot.users import views

urlpatterns = patterns('',
	url(r'^login/', views.login_view, name='login_view'),
	url(r'^auth/', views.auth_user, name='auth_user'),
	url(r'^register/', views.register_view, name='register_view'),
	url(r'^add/', views.add_user, name='add_user')
)

