from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^city/(?P<city_id>[0-9]+)/$', views.getGurukulByCity, name='getGurukulByCity'),
    url(r'^gurukul/(?P<gurukul_id>[0-9]+)/$', views.getStudentByGurukul, name='getStudentByGurukul'),
    url(r'^student/(?P<student_id>[0-9]+)/$', views.getStudentInfo, name='getStudentInfo'),
    url(r'^sp/(?P<sponsor_id>[0-9]+)/$', views.getSponsorInfo, name='getSponsorInfo'),
]
