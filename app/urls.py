from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    url(r'^$', views.contact_view, name="contact"),
    url(r'^requests/$', views.request_view, name="requests"),
)
