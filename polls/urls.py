#-*- coding: utf-8 -*-
from django.urls import re_path

from . import views

app_name = "polls"
urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    re_path(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    re_path(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
]
