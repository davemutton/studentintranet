from django.shortcuts import render, render_to_response
from django.views.generic import CreateView
from mediamanager.models import LearningObject, FileResource
from forms import UploadFileForm
from mediamanager.forms import FileResourceForm
from django.template import RequestContext
# Create your views here.

class createLearningobject(CreateView):
	model = LearningObject
	template_name = 'mediamanager/edit_learningobject.html'
	def get_success_url(self):
		return reverse('index')
	fields =['title','archivefile','tags','pathway','level','agebracket']

class createFileResource(CreateView):
	model = LearningObject
	template_name = 'mediamanager/edit_learningobject.html'
	def get_success_url(self):
		return reverse('index')
	fields =['title','tags','pathway','level','agebracket']\


def FileResourceFormView(request):
	if request.method == 'GET':
		form = FileResourceForm()
	else:
		form = FileResourceForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			post = Page.objects.create(title=title)
			return HttpResponseRedirect(reverse('index', ))
	return render(request, 'mediamanager/file_upload.html', {'form': form,})


def test(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print "request.FILES"
        if form.is_valid():
            new_file = UploadFile(file = request.FILES['file'])
            new_file.save()
 
            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UploadFileForm()
 
    data = {'form': form}
    return render_to_response('mediamanager/test.html', data, context_instance=RequestContext(request))