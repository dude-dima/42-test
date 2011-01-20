from django.conf.urls.defaults import patterns, include
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^logout/$', views.logout_view),
    (r'^main/$', views.contact_view),
    (r'^requests/$', views.request_view),
    (r'^edit/$', views.edit_view),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'^accounts/login/$', 'django.contrib.auth.views.login',
                                {'template_name': 'login.html'}),
)
