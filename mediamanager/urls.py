from django.conf.urls import patterns, include, url
from django.contrib import admin
from mediamanager import views

urlpatterns = patterns('',
	
#urls for adding resources
	url(r'^edit/learningobject/(?P<pk>\d+)', views.UpdateLearningObject, name='learningobject-edit',),
	url(r'^edit/learningobject/', views.CreateLearningObject, name='learningobject-new',),
    url(r'^edit/fileresource/(?P<pk>\d+)', views.UpdateFileResource, name='fileresource-edit',),
    url(r'^create/fileresource/', views.CreateFileResource, name='fileresource-new',),
    url(r'^create/urlresource/', views.CreateURLResource, name='urlresource-new',),




#search indexing
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.index, name='index'),





 





# testing file uploads  
    url(r'^test/', views.test, name='test'),
#this url displays individual resources
    url(r'^view/default/(?P<default_resource_slug>[\w\-]+)/', views.defaultresourceview, name='defaultpageview'),
    url(r'^view/file/(?P<resource_slug>[\w\-]+)/', views.fileresourceview, name='filepageview'),
    
	)
