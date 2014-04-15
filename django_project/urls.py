from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django_project import settings
from rest_framework import routers
from django.contrib import admin
from translately import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'accounts', views.AccountViewSet)
# router.register(r'documents', views.DocumentViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root', settings.STATICFILES_DIRS}
    ),
    url(r'^translately/', include('translately.urls')),
    url(r'^admin/', include(admin.site.urls))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
