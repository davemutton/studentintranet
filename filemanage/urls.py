from django.conf.urls import patterns, include, url

from django.contrib import admin
from filemanage import views
from django.views.decorators.csrf import csrf_exempt   
urlpatterns = patterns('',
	

	

#  file uploads  
    url(r'^upload/', csrf_exempt(views.FileUpload), name='file_upload'),
    url(r'^$', views.index, name='index_test'),
    url(r'^query/singlefile/(?P<pk>\d+)', views.QuerySingleFile, name='learningobject-edit',),

	)
