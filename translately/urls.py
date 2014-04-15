__author__ = 'matt'
from django.conf.urls import patterns, url
from translately import api
from translately import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^api/accounts/$', api.AccountList.as_view()),
    url(r'^api/accounts/(?P<pk>\d+)/$', api.AccountDetail.as_view()),

    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<pk>\d+)/vote/$', views.vote, name='vote'),

)

urlpatterns = format_suffix_patterns(urlpatterns)