__author__ = 'matt'
from django.conf.urls import patterns, url

from translately import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<account_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<account_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<account_id>\d+)/vote/$', views.vote, name='vote'),
)