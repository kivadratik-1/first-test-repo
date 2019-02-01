from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.guest_new, name='guest_new'),
    url(r'^guest/list/$', views.guest_list, name='guest_list'),
]
