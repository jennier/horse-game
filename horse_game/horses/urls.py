from django.conf.urls import url
from django.contrib import admin

from .views import (
	HorseList,
	HorseCreate,
	HorseDetail,
	horse_update,
	horse_delete,
	)

urlpatterns = [
	url(r'^$', HorseList.as_view(), name='list'),
    url(r'^create/$', HorseCreate.as_view(), name='create'),
    url(r'^(?P<pk>[\w-]+)/$', HorseDetail.as_view(), name='detail'),
    url(r'^(?P<pk>[\w-]+)/edit/$', horse_update, name='update'),
    url(r'^(?P<pk>[\w-]+)/delete/$', horse_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
