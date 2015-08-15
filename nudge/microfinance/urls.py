from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.students),
    url(r'^/sponsor(?P<sponsor_id>[0-9]+)/$', views.sponsor, name='get_sponsor_info')
]
