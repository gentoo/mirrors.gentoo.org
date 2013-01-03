from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'mirrors.views.index'),
    url(r'^contacts/$', 'mirrors.views.contacts'),
                       )

urlpatterns += staticfiles_urlpatterns()
