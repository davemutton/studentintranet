from django.shortcuts import render
from django.views.generic import CreateView
from mediamanager.models import LearningObject
from mediamanager.forms import FileResourceForm
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


