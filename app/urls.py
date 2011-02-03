from django.conf.urls.defaults import patterns, include, url
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.contact_view, name="contact"),
    url(r'^requests/$', views.request_view, name="requests"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^edit/$', views.edit_view, name="edit"),
    url(r'^tag/$', views.tag_view, name="tag"),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login',
                                {'template_name': 'login.html'}),
)
