from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^sponsorInfo/(?P<sponsor_id>[0-9]+)/$',
        views.sponsorInfo, name='get-sponsor-info'),
    url(r'^list/$',
        views.studentListing, name="students-list"),
    url(r'^student/(?P<student_id>[0-9]+)$',
        views.student, name="student"),
    url(r'^investmentHistory/?P<sponsor_id>[0-9]+)/$', views.investmentHistory, name="investment-history")
]
