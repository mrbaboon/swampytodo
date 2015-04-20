from django.conf.urls import patterns, url

urlpatterns = patterns('todo.views',
    url('^$', 'todo_view', name='todo'),
)