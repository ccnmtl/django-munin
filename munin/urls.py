try:
    from django.conf.urls import patterns
except ImportError:
    from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
                       (r'^total_users/$', 'munin.views.total_users'),
                       (r'^active_users/$', 'munin.views.active_users'),
                       (r'^total_sessions/$', 'munin.views.total_sessions'),
                       (r'^active_sessions/$', 'munin.views.active_sessions'),
                       (r'^db_performance/$', 'munin.views.db_performance'),
)
