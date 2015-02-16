from mediamanager.models import LearningObject, FileResource
from django import forms
from mediamanager.fields import MultiFileField

class FileResourceForm(forms.Form):
	title = forms.CharField(max_length=100)
	files = MultiFileField(max_num = 10, min_num = 1, maximum_file_size = 1024*1024*5)

