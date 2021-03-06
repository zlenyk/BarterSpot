from django.conf.urls import patterns, include, url
import settings
from django.conf.urls.static import static


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BarterSpot.views.home', name='home'),
    # url(r'^BarterSpot/', include('BarterSpot.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^searchUser/', 'BarterSpot.views.search'),
    url(r'^searchAnnouncements/', 'BarterSpot.views.searchAnnouncements'),
    url(r'^searchPanel/', 'BarterSpot.views.searchPanel'),
    url(r'^$', 'BarterSpot.views.index'),
    url(r'^announcements/', include('BarterSpot.announcements.urls')),
    url(r'^users/', include('BarterSpot.users.urls')),
    url(r'^messages/', include('BarterSpot.messages.urls')),
    url(r'^transactions/', include('BarterSpot.transactions.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
