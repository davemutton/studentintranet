from django.shortcuts import render, render_to_response
from django.views.generic import CreateView
from mediamanager.models import LearningObject, FileResource, AttachedFiles, DefaultResource,AssoeLevel
from forms import UploadFileForm
from django.http import HttpResponseRedirect
from mediamanager.forms import FileResourceForm, LearningObjectuploadform
from django.template import RequestContext
from django.core.urlresolvers import reverse
from taggit.models import Tag
import sys
# Create your views here.

def createLearningobject(request):
	if request.method == 'GET':
		form = LearningObjectuploadform()
	else:
		form = LearningObjectuploadform(request.POST, request.FILES)
		if form.is_valid():
			print form.cleaned_data
			learningobject = request.FILES['archivefile']
			title = form.cleaned_data['title']
			description = form.cleaned_data['description']
			tags = form.cleaned_data['tags']
			levels = form.cleaned_data['level']
			pathways = form.cleaned_data['pathway']
			agebrackets = form.cleaned_data['agebracket']
			post = LearningObject.objects.create(archivefile=learningobject,title=title, description=description)
			for tag in tags:
				post.tags.add(tag)
			for level in levels:
				post.level.add(level.pk)
			for pathway in pathways:
				post.pathway.add(pathway.pk)
			for agebracket in agebrackets:
				post.agebracket.add(agebracket.pk)
			post.save()
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
	exclusiveurltags = request.GET.get('extag', False)
	urltags = request.GET.get('tag', False)
	urlpathwaylist =[]
	if urltags:
		urltagslist = urltags.split("/")
		default_resource_list =[]
		for tag in urltagslist:
			print tag
			for objects in DefaultResource.objects.filter(tags__name__in=urltagslist):
				default_resource_list.append(objects)
		default_resource_list = list(set(default_resource_list))
		default_resource_list.sort(key=lambda x: x.score, reverse=True)
		
	else:
		default_resource_list = DefaultResource.objects.order_by('-score')
#Start exclusive keyword tags		
	if exclusiveurltags:
		for objects in default_resource_list:
			print objects.tags.names()
			for tag in objects.tags.names():
				print tag

#end exclusive keyword tags		
	

	urlpathway = request.GET.get('pathway', False)
	urlpathwayfiltered_list = []
	if urlpathway:
		urlpathwaylist = urlpathway.split("/")
		print urlpathwaylist
		for objects in default_resource_list:
			for taggedpathway in objects.pathway.all():
				print taggedpathway.pathway
				print "1!"
				for pathway in urlpathwaylist:
					print type(pathway) 
					print type(taggedpathway.pathway)
					if pathway == str(taggedpathway):
						urlpathwayfiltered_list.append(objects)
		default_resource_list = urlpathwayfiltered_list
		default_resource_list = list(set(default_resource_list))
		default_resource_list.sort(key=lambda x: x.score, reverse=True)

	urlage = request.GET.get('age', False)
	urlagefiltered_list = []
	if urlage:
		urlagelist = urlage.split("/")
		print urlagelist
		for objects in default_resource_list:
			for taggedage in objects.agebracket.all():
				for age in urlagelist:
					if age == str(taggedage):
						urlagefiltered_list.append(objects)
		default_resource_list = urlagefiltered_list
		default_resource_list = list(set(default_resource_list))
		default_resource_list.sort(key=lambda x: x.score, reverse=True)
	for objects in default_resource_list:
		print objects
		print objects.tags.all()
		for each in objects.tags.all():
			print objects
			print objects.tags.all()
			print each
			print each.name

	









	
	context_dict = {'default_resource_list':default_resource_list}
	return render_to_response('mediamanager/index.html', context_dict, context)


def defaultresourceview(request, default_resource_slug):
	#
	#This view displays an individual resource
	#
	context_dict = {}
	try:
		default_resource = DefaultResource.objects.get(slug=default_resource_slug)

		default_resource.views = default_resource.views + 1
		default_resource.save()
		print default_resource.views
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