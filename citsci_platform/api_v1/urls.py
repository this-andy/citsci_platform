from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^public/$', views.public),
    url(r'^private/$', views.private),
    url(r'^projects-public/$', views.ProjectListAPIView.as_view(), name='project_list_api_public'),
    url(r'^projects-private/$', views.ProjectListAPIViewPrivate.as_view(), name='project_list_api_private'),
    url(r'^projects-scoped/$', views.ProjectListAPIViewScoped.as_view(), name='project_list_api_scoped'),
    url(r'^projects/(?P<id>[-\w]+)/$', views.ProjectRetrieveUpdateAPIView.as_view(), name='project_get_api'),
]
