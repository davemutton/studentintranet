from django.conf.urls import patterns, include, url
from django.contrib import admin
from users import views

urlpatterns = patterns('',
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
    )
#urls for adding resources
	