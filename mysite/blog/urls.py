# -*- coding: utf-8 -*-
'''
Created on 2018年1月30日

@author: zp
'''

from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.post_list, name='post_list'),
]