from django.conf.urls import patterns, include, url
from django.contrib import admin
from wiki import views

urlpatterns = patterns('',
	url(r'^new/page', views.createPage.as_view(), name='page-new',),
	url(r'^new/learningobject', views.createLearningobject.as_view(), name='learningobject-new',),
	url(r'^createpage/(\d+)', views.page_form, name='page-form'),
	url(r'^createlearningobject/(\d+)', views.learningobject_form, name='learningobject_form'),
	url(r'^page/(?P<default_page_slug>[\w\-]+)/', views.defaultpageview, name='defaultpageview'),
	url(r'^$', views.index, name='index'),

    
	)
