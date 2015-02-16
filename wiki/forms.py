from froala_editor.widgets import FroalaEditor
from wiki.models import LearningObject
from django import forms

class PageForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=FroalaEditor)

class LearningObjectForm(forms.ModelForm):
	class Meta:
		model = LearningObject
		fields = ['title','archivefile']
