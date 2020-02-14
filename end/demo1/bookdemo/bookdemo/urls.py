"""bookdemo URL Configuration

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
from django.urls import path,include

# 路由 网址 每一个网址均需要绑定视图函数 视图函数给与页面返回
# MVT V视图函数  3个作用 接收请求 处理数据 返回数据

from django.http import  HttpResponse
def index(res):
    return HttpResponse("这里是首页")

def list(res):
    return HttpResponse("这里是详情页")

def jsondata(res):
    return HttpResponse("{'name':'zml','age':'20'}")
urlpatterns = [
    path('admin/', admin.site.urls),
    # 使用path将booktest的路由进行包含
    path('booktest/',include('booktest.urls')),
    # 将index路由与index视图函数绑定
    path("index/",index),
    path("list/",list),
    path("json/",jsondata)
]


# 所有路由地址配置文件
# admin路由是Django自带的后台管理路由

# 总的路由匹配文件  项目路由文件  使用include包含应用路由文件