from django.urls import re_path

from munin.views import total_users, active_users, total_sessions, \
    active_sessions, db_performance

urlpatterns = [
    re_path(r'^total_users/$', total_users),
    re_path(r'^active_users/$', active_users),
    re_path(r'^total_sessions/$', total_sessions),
    re_path(r'^active_sessions/$', active_sessions),
    re_path(r'^db_performance/$', db_performance),
]
