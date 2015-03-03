from django.conf.urls import patterns, include, url
from django.contrib import admin
from mediamanager import views

urlpatterns = patterns('',
	
#urls for adding resources
	url(r'^new/learningobject', views.createLearningobject, name='learningobject-edit',),
    url(r'^new/fileresource', views.FileResourceFormView, name='fileresource-edit',),





#search indexing
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.index, name='index'),











# testing file uploads  
    url(r'^test/', views.test, name='test'),
#this url displays individual resources
    url(r'^view/(?P<default_resource_slug>[\w\-]+)/', views.defaultresourceview, name='defaultpageview'),

	)
