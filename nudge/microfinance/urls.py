from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^/sponsor(?P<sponsor_id>[0-9]+)/$',
        views.sponsor, name='get-sponsor-info'),
    url(r'^/students/$',
        views.studentListing, name="students-list"),
]
