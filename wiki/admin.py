from django.contrib import admin
from wiki.models import Page, LearningObject, AdminPage, SubjectPage



# Register your models here.
admin.site.register(SubjectPage)
admin.site.register(Page)
admin.site.register(AdminPage)
admin.site.register(LearningObject)