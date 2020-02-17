# 引入路由绑定函数
from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$',views.index2,name='index2'),
    url(r'^detail2/(\d+)/$',views.detail2,name='detail2'),
    url(r'^result/(\d+)/$',views.result,name='result'),
]