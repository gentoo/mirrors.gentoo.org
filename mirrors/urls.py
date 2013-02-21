from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^$', 'mirrors.views.index'),
    (r'^settings/$', 'mirrors.views.settings'),
    (r'^settings/add/provider/$', 'mirrors.views.settings_add_provider'),
    (r'^settings/add/contact/$', 'mirrors.views.settings_add_contact'),
    (r'^settings/add/portagemirror/$', 'mirrors.views.settings_add_portagemirror'),
    (r'^settings/add/distfilesmirror/$', 'mirrors.views.settings_add_distfilesmirror')
)

urlpatterns += staticfiles_urlpatterns()
