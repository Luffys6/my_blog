"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from django.views.static import serve
from my_blog.settings import STATICFILES_DIRS, MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),


    # 配置mdeditor路由
    path(r'mdeditor/', include('mdeditor.urls')),
    # django关闭debug模式后，静态文件无法访问，这里要设置下静态文件的访问路由
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATICFILES_DIRS}),
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

]
