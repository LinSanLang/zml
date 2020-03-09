"""Taoku URL Configuration

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
from shopapp.views import *
from django.conf.urls import url
from django.views.static import serve
from .settings import MEDIA_ROOT
# 引入API文档路由
from rest_framework.documentation import include_docs_urls

# 引入rest_framework_simplejwt路由
# from rest_framework_simplejwt.views import token_obtain_pair
# from rest_framework_simplejwt.views import token_refresh


# 引入jwt路由
# from rest_framework_jwt.views import obtain_jwt_token

# 引入DRF自带的路由类
from rest_framework import routers
router = routers.DefaultRouter()

# 可以通过router默认路由资源
router.register('categorys',CategoryViewSets)
router.register('goods',GoodViewSets)
router.register('goodimgs',GoodImgsViewSets)
# router.register('users',UserViewSets)
# router.register('orders',OrderViewSets)
router.register('flashs',FlashViewSets)
router.register('kills',KillViewSets)
router.register('internations',InternationViewSets)
router.register('taokushops',TaokushopViewSets)



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # 配置RestFulApi
    path('api/v1/',include(router.urls)),
    # 为了在DRF路由调试界面能够使用用户相关功能 需要引入以下路由
    path('', include('rest_framework.urls')),
    # API文档路由
    path('api/v1/docs/',include_docs_urls(title='RestFulAPI',description='RestFulAPI v1')),
]
