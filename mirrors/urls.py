from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^$', 'mirrors.views.index'),
    (r'^settings/$', 'mirrors.views.settings'),
)

urlpatterns += staticfiles_urlpatterns()
