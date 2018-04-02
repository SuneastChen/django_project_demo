# _*_ coding:utf-8 _*_
# !/usr/bin/python

from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index/$', views.index),
    url('^(\d+)/$', views.detail),
    url(r'^boots/$', views.bootstrap),
]