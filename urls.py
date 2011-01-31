from django.conf.urls.defaults import patterns, include
import os


urlpatterns = patterns('',

    (r'', include('app.urls')),

    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__),
                                       "templates/css").replace('\\', '/')}),
)
