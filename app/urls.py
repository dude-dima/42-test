from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^$', views.contact_view),
    (r'^requests/$', views.request_view),
)
