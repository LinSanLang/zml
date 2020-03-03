"""drfend URL Configuration

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
from shop.views import *
from django.conf.urls import url
from django.views.static import serve
from .settings import MEDIA_ROOT
# 引入API文档路由
from rest_framework.documentation import include_docs_urls
# 引入DRF自带的路由类
from rest_framework import routers
router = routers.DefaultRouter()

# 可以通过router默认路由资源
router.register('categorys',CategoryViewSets)
router.register('goods',GoodViewSets)
router.register('goodimgs',GoodImgsViewSets)
router.register('users',UserViewSets)
router.register('orders',OrderViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # 配置RestFulApi
    path('api/v1/',include(router.urls)),
    # 为了在DRF路由调试界面能够使用用户相关功能 需要引入以下路由
    path('', include('rest_framework.urls')),
    # API文档路由
    path('api/v1/docs/',include_docs_urls(title='RestFulAPI',description='RestFulAPI v1')),

    # url(r'^categorylist/$',CategoryListView.as_view(),name='categorylist'),
    # url(r'^categorydetail/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name='categorydetail'),
    #
    # url(r'^categorys/$',CategoryViewSets2.as_view({'get':'list','post':'create'})),
    # url(r'^categorys/(?P<pk>\d+)/$',CategoryViewSets2.as_view({'get':'retrieve','put':'update','patch':'update','delete':'destroy'})),

]
