#_*_coding:utf8_*_

from django.conf.urls import url, include
from . import views
app_name = 'polls'
urlpatterns = [
    # /polls/
    url(r'^$', views.index, name='index'),
    # /polls/1/
    url(r'^(\d+)/$', views.detail, name='detail'),
    # /polls/1/results/
    url(r'^(\d+)/results/$', views.results, name='results'),
    # /polls/1/vote/
    url(r'^(\d+)/vote/$', views.vote, name='vote'),
]
