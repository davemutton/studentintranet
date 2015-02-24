from django.shortcuts import render, render_to_response
from django.views.generic import CreateView
from mediamanager.models import LearningObject, FileResource, AttachedFiles, DefaultResource
from forms import UploadFileForm
from django.http import HttpResponseRedirect
from mediamanager.forms import FileResourceForm, LearningObjectuploadform
from django.template import RequestContext
from django.core.urlresolvers import reverse
import sys
# Create your views here.

def createLearningobject(request):
	print request.POST
	if request.method == 'GET':
		form = LearningObjectuploadform()
	else:
		print request.POST
		form = LearningObjectuploadform(request.POST, request.FILES)
		print form.errors.as_data()
		if form.is_valid():
			print form.cleaned_data
			learningobject = request.FILES['archivefile']
			title = form.cleaned_data['title']
			description = form.cleaned_data['description']
			print form.cleaned_data
			post = LearningObject.objects.create(archivefile=learningobject,title=title, description=description)
			return HttpResponseRedirect(reverse('index', ))
		else:
			print "form not valid"
	return render(request, 'mediamanager/edit_learningobject.html', {'form': form,})

class createFileResource(CreateView):
	model = LearningObject
	template_name = 'mediamanager/edit_learningobject.html'
	def get_success_url(self):
		return reverse('index')
	fields =['title','tags','pathway','level','agebracket']

def index(request):
	context = RequestContext(request)
	default_resource_list = DefaultResource.objects.order_by('-score')
	context_dict = {'default_resource_list':default_resource_list}
	return render_to_response('mediamanager/index.html', context_dict, context)


def defaultresourceview(request, default_resource_slug):
	#
	#This view displays an individual resource
	#
	context_dict = {}
	try:
		default_resource = DefaultResource.objects.get(slug=default_resource_slug)

		default_resource.score = default_resource.score + 1
		default_resource.save()
		print default_resource.score
		context_dict['default_resource'] = default_resource
	except:
		pass
	return render(request,'mediamanager/default_resource.html',context_dict)


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
        if form.is_valid():
            new_file = AttachedFiles.objects.create(attachedfiles=request.FILES['file'])
            new_file.save()
            print "got to here"
 
            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UploadFileForm()
 
    data = {'form': form}
    return render_to_response('mediamanager/test.html', data, context_instance=RequestContext(request))