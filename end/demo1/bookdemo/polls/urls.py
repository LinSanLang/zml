# 引入路由绑定函数
from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$',views.index2,name='index2'),
    # url(r'^$',views.IndexView.as_view(),name='index2'),
    url(r'^detail2/(\d+)/$',views.detail2,name='detail2'),
    url(r'^result/(\d+)/$',views.result,name='result'),
    url(r'^login',views.login,name='login'),
    url(r'^regist',views.regist,name='regist'),
    url(r'^logout',views.logout,name='logout'),
    # url(r'^detail2/(?P<qid>\d+)/$',views.DetailView.as_view(),name='detail2'),
    # url(r'^result/(\d+)/$',views.ResultView.as_view(),name='result')

]