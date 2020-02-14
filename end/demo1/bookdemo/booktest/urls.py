# 引入路由绑定函数
from django.conf.urls import url
from . import views

app_name = 'booktest'

urlpatterns = [
    # url(r'^index/$',views.index),
    # 使用正则分组可以向试图函数传递参数
    # 第一个参数就是路由 第二个参数就是视图函数
    # 第一个参数章如果有正则分组 小括号 则正则分组匹配的内容就会作为实参传递给视图函数
    url(r'detail/(\d+)/',views.detail,name='detail'),
    url(r'^$',views.index,name='index'),
    url(r'^deletebook/(\d+)/$',views.deletebook,name='deletebook'),
    url(r'^deletehero/(\d+)/$',views.deletehero,name='deletehero'),
    url(r'^edithero/(\d+)/$',views.edithero,name='edithero'),
    url(r'^addhero/(\d+)/$',views.addhero,name='addhero'),
    url(r'^addbook/$',views.addbook,name='addbook'),
    url(r'^editbook/(\d+)/$',views.editbook,name='editbook')
]