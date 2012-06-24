from django.conf.urls import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', views.main),
        url(r'^signup$', views.signup),
        url(r'^thanks$', views.thanks),
    # Examples:
    # url(r'^$', 'hw2.views.home', name='home'),
    # url(r'^hw2/', include('hw2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
