from mediamanager.models import LearningObject, FileResource,AssoeLevel,AssoePathway,AgeBracket,AssoeSubjects
from django import forms
from mediamanager.fields import MultiFileField
from filemanage.models import AttachedFiles
 



 
class FileResourceForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    level = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=None,required=True)
    agebracket =forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=None,required=True)
    pathway = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=None,required=True)
    subject = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=None,required=True)
    class Meta:
        model = FileResource
        fields =['title','pathway','level','subject','agebracket','tags','description']

    def __init__(self, *args, **kwargs):
        super(FileResourceForm, self).__init__(*args, **kwargs)
        self.fields['level'].queryset = AssoeLevel.objects.all()
        self.fields['pathway'].queryset = AssoePathway.objects.all()
        self.fields['agebracket'].queryset = AgeBracket.objects.all()
        self.fields['subject'].queryset = AssoeSubjects.objects.all()



class LearningObjectuploadform(forms.ModelForm): 
        level = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=None,required=False)
        agebracket =forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=None,required=False)
        pathway = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=None,required=False)
        subject = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=None,required=True)

        class Meta: 
            model = LearningObject 
            fields =['title','archivefile','description','tags','pathway','level','subject','agebracket','description']
                 
        def __init__(self, *args, **kwargs):
            super(LearningObjectuploadform, self).__init__(*args, **kwargs)
            self.fields['level'].queryset = AssoeLevel.objects.all()
            self.fields['pathway'].queryset = AssoePathway.objects.all()
            self.fields['agebracket'].queryset = AgeBracket.objects.all()
            self.fields['subject'].queryset = AssoeSubjects.objects.all()


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
