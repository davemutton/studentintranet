from django.contrib import admin
from mediamanager.models import AssoeLevel, AssoePathway, AgeBracket, LearningObject, AttachedFiles, FileResource,VideoResource,AssoeSubjects
# Register your models here.

class FileAttachedInline(admin.TabularInline):
	model = AttachedFiles

class FileResourceAdmin(admin.ModelAdmin):
	inlines = [
	FileAttachedInline,
	]

admin.site.register(FileResource, FileResourceAdmin)	
admin.site.register(AssoeLevel)
admin.site.register(AssoePathway)
admin.site.register(AgeBracket)
admin.site.register(LearningObject)
admin.site.register(AttachedFiles)
admin.site.register(VideoResource)
admin.site.register(AssoeSubjects)

