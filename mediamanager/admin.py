from django.contrib import admin
from mediamanager.models import AssoeLevel, AssoePathway, AgeBracket, LearningObject, FileResource,VideoResource,AssoeSubjects,UrlResource
# Register your models here.


admin.site.register(FileResource)	
admin.site.register(AssoeLevel)
admin.site.register(AssoePathway)
admin.site.register(AgeBracket)
admin.site.register(LearningObject)
admin.site.register(VideoResource)
admin.site.register(AssoeSubjects)
admin.site.register(UrlResource)
