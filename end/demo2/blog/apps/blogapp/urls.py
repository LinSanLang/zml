
from django.conf.urls import url
from . import views
from .feed import ArticleFeed
from django.urls import include
app_name = 'blogapp'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^rss/$',ArticleFeed(),name='rss'),
    url(r'^search/', include('haystack.urls')),
    # 配置ico图标
    url(r'^favicon.ico$',views.favicon),
]