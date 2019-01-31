from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.guest_list, name='guest_list'),
    url(r'^guest/new/$', views.guest_new, name='guest_new'),
]
