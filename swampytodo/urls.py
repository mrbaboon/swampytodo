from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'swampytodo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^monitor', 'monitor.views.monitor_view', name='monitor'),

    url(r'^todo', include('todo.urls', namespace='todo')),
    url(r'^admin/', include(admin.site.urls)),
)
