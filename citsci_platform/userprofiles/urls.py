from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create', views.UserProfileCreateView.as_view(), name='createprofile'),
    url(r'^edit/(?P<pk>[0-9a-f-]+)/$', views.UserProfileUpdateView, name ='editprofile'),
    url(r'^view/(?P<pk>[0-9a-f-]+)/$', views.UserProfileDetailView.as_view(), name ='viewprofile'),

]
