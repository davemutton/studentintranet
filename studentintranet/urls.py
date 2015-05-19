from django.conf.urls import patterns, include, url
from django.contrib import admin
from wiki import views
from updown.views import AddRatingFromModel
urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # end examples
    url(r'^wiki/', include('wiki.urls')),
    url(r'^mediamanager/',include('mediamanager.urls')),
    url(r'^filemanage/', include('filemanage.urls')),
    #for admin
    url(r'^admin/', include(admin.site.urls)),

    #for third party apps
    url(r'^froala_editor/', include('froala_editor.urls')),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url(r"^(?P<object_id>\d+)/rate/(?P<score>[\d\-]+)$", AddRatingFromModel(), {'app_label': 'mediamanager','model': 'DefaultResource','field_name': 'updownvotes',}, name="resource_updownvotes"),

    
)
