from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^list', views.photo_list, name='Photo list'),
    url(r'^list', views.IndexView.as_view(), name='Photo list GV'),
    url(r'^photo_edit', views.photo_edit, name='pictures2'),
    url(r'^item/(?P<photo_slug>[\w\-]+)/$', views.photo_details, name ='Photo details'),
    url(r'^zoom', views.photo_zoom, name='Picture zoom'),
]
