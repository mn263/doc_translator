from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django_project import settings
from django.contrib import admin
from translately import api

admin.autodiscover()

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
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'),),

  url(r'', include('translately.urls')),
  url(r'^translately/', include('translately.urls')),
) + static(settings.MEDIA_URL)