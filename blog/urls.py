# encoding: utf-8
'''
@author: dbj
@file: urls.py
@time: 2021/4/2 11:42
@desc:
'''
from django.urls import path
from blog.views import IndexView, DetailView

urlpatterns = [
    # 首页的路由 即什么路径都不写就会跳转到首页
    path('index/', IndexView.as_view(), name='index'),
    path('detail/', DetailView.as_view(), name='detail'),
]