from django.conf.urls import patterns, include, url
from django.contrib import admin
from mediamanager import views

urlpatterns = patterns('',
	url(r'^new/learningobject', views.createLearningobject.as_view(), name='learningobject-new',),
    url(r'^new/fileresource', views.FileResourceFormView, name='fileresource-new',),
	)
