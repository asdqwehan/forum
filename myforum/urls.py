from django.conf.urls import include, url
from myforum import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(\d+)/$', views.bbs_detail, name='detail'),
    url(r'^detail/(\d+)/comments/$', views.comments, name='comments'),
]