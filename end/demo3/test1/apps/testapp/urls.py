from django.conf.urls import url
from . import views

app_name = 'testapp'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^details/(\d+)/$',views.details,name='detail'),
    url(r'^whisper/$', views.whisper, name='whisper'),
    url(r'^leacots/$', views.leacots, name='leacots'),
    url(r'^album/$', views.album, name='album'),
    url(r'^about/$', views.about, name='about'),
]