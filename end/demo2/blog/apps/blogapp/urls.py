
from django.conf.urls import url
from . import views

app_name = 'blogapp'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^contact/$', views.contact, name='contact'),

    # 配置ico图标
    url(r'^favicon.ico$',views.favicon),
]