from mediamanager.models import LearningObject, FileResource,AssoeLevel,AssoePathway,AgeBracket
from django import forms
from mediamanager.fields import MultiFileField

 
class UploadFileForm(forms.ModelForm):
     
    class Meta:
        model = FileResource
        fields =['title']



class FileResourceForm(forms.Form):
	title = forms.CharField(max_length=100)
	files = MultiFileField(max_num = 10, min_num = 1, maximum_file_size = 1024*1024*5)



class LearningObjectuploadform(forms.ModelForm): 
        level = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=None,required=False)
        agebracket =forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=None,required=False)
        pathway = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=None,required=False)
        class Meta: 
            model = LearningObject 
            fields =['title','archivefile','description','tags','pathway','level','subject','agebracket']
                 
        def __init__(self, *args, **kwargs):
        	super(LearningObjectuploadform, self).__init__(*args, **kwargs)
        	self.fields['level'].queryset = AssoeLevel.objects.all()
        	self.fields['pathway'].queryset = AssoePathway.objects.all()
        	self.fields['agebracket'].queryset = AgeBracket.objects.all()

class LearningObjectuploadform2(LearningObjectuploadform): 
        archivefile = forms.FileField(required=False)
        class Meta: 
            model = LearningObject 
            fields =['title','archivefile','description','tags','pathway','level','subject','agebracket']
                 
        def __init__(self, *args, **kwargs):
            super(LearningObjectuploadform, self).__init__(*args, **kwargs)
            self.fields['level'].queryset = AssoeLevel.objects.all()
            self.fields['pathway'].queryset = AssoePathway.objects.all()
            self.fields['agebracket'].queryset = AgeBracket.objects.all()
