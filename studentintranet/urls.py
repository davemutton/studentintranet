from django.conf.urls import patterns, include, url
from django.contrib import admin
from wiki import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # end examples
    url(r'^wiki/', include('wiki.urls')),
    url(r'^mediamanager/',include('mediamanager.urls')),
    #for admin
    url(r'^admin/', include(admin.site.urls)),

    #for third party apps
    url(r'^froala_editor/', include('froala_editor.urls')),
    (r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    
)
