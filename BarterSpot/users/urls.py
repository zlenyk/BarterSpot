from django.conf.urls import patterns, url
from BarterSpot.users import views

urlpatterns = patterns('',
	url(r'^login/', views.login_view, name='login_view'),
	url(r'^auth/', views.auth_user, name='auth_user')
)

