from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hubspot_auth_page, name='hubspot auth'),
]
