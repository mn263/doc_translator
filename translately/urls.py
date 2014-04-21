__author__ = 'matt'
from django.conf.urls import patterns, url
from translately import views, api
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
  url(r'^api/user-auth/', 'rest_framework_jwt.views.obtain_jwt_auth'),
  url(r'^api/user-create/', 'rest_framework_jwt.views.create_jwt_user'),
  url(r'^api/user-delete/', 'rest_framework_jwt.views.delete_jwt_user'),
  url(r'^api/user-update-username/', 'rest_framework_jwt.views.change_jwt_username'),
  url(r'^api/user-update-email/', 'rest_framework_jwt.views.change_jwt_email'),
  url(r'^api/user-update-password/', 'rest_framework_jwt.views.change_jwt_password'),
  url(r'^api/user-get/username=(?P<username>[a-z0-9-]+)/password=(?P<password>[a-z0-9-]+)$', api.UserDetail.as_view()),
  url(r'^api/documents-get/username=(?P<username>[a-z0-9-]+)/password=(?P<password>[a-z0-9-]+)$', api.DocumentDetail.as_view()),
  url(r'^api/document-add/$', 'rest_framework_jwt.views.add_jwt_document'),
  url(r'^api/document-delete/$', 'rest_framework_jwt.views.remove_jwt_document'),
  url(r'^api/user-get-documents/$', 'rest_framework_jwt.views.change_jwt_password'),
  # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'),),

  url(r'^$', views.index, name='index'),)
urlpatterns = format_suffix_patterns(urlpatterns)