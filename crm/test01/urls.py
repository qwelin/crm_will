# _*_ coding:utf-8 _*_

__author__ = "will"
__data__ = "2017/11/12 23:53"

from django.conf.urls import url
from test01 import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^student_index/$', views.student_index,name='student_index'),
    url(r'^teacher_index/$', views.teacher_index,name='teacher_index'),
    url(r'^customer_index/$', views.customer_index,name='customer_index'),
    url(r'^sale_index/$', views.sale_index,name='sale_index'),
    url(r'^customerfollowuo/$', views.customerfollowup,name='customerfollowup'),
]

# 销售 sale_index customer_index
# 老师 teacher_index
# 主任 sale_index student_index leader_index teacher_index customer_index
# 学生 student_index