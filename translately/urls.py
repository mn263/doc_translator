__author__ = 'matt'
from django.conf.urls import patterns, url
from translately import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('', url(r'^$', views.index, name='index'), )
urlpatterns = format_suffix_patterns(urlpatterns)