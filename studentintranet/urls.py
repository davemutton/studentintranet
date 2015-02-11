from django.conf.urls import patterns, include, url
from django.contrib import admin
from wiki import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studentintranet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^wiki/', include('wiki.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^summernote/', include('django_summernote.urls')),
    url(r'^froala_editor/', include('froala_editor.urls')),
    
)
