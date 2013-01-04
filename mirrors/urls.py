from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^$', 'mirrors.views.index'),
    (r'^settings/$', 'mirrors.views.settings'),
    (r'^settings/add/provider/$', 'mirrors.views.settings_add_provider'),
    (r'^settings/add/contact/$', 'mirrors.views.settings_add_contact'),
)

urlpatterns += staticfiles_urlpatterns()
