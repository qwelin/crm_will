# _*_ coding:utf-8 _*_

__author__ = "will"
__data__ = "2017/11/12 23:53"

from django.conf.urls import url
from test01 import views

urlpatterns = [
    url(r'^index/', views.index),
]