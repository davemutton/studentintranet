from django.shortcuts import render, render_to_response
from django.views.generic import CreateView
from mediamanager.models import LearningObject, FileResource, DefaultResource, AssoeLevel, AgeBracket, AssoePathway, AssoeSubjects

from django.http import HttpResponseRedirect, HttpResponse
from mediamanager.forms import FileResourceForm, LearningObjectuploadform, LearningObjectuploadform2
from django.template import RequestContext
from django.core.urlresolvers import reverse
from taggit.models import Tag
import sys, json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView
from itertools import chain
from filemanage.models import AttachedFiles

 #Create your views here.

class CreateLearningObject(CreateView):
	model = LearningObject
	template_name = 'mediamanager/edit_learningobject.html'
	def get_success_url(self):
		return reverse('index')

class UpdateLearningObject(UpdateView):
	model = LearningObject
	template_name = 'mediamanager/edit_learningobject.html'
	def get_success_url(self):
		return reverse('index')
'''
class UpdateFileResource(UpdateView):
	model = FileResource
	template_name = 'mediamanager/edit_fileresource.html'
	def get_success_url(self):
		return reverse('index')
'''

def UpdateFileResource(request,pk):
	instance = FileResource.objects.get(pk=pk)
	context = RequestContext(request)
	if request.method == 'POST':
		form = FileResourceForm(request.POST,instance=instance)
		if form.is_valid():
			newobject = form.save()
			filesattached = request.POST.get('filesattached',False)
			if filesattached:
				if filesattached[-1:] == ",":
					filesattached = filesattached[:-1]
				filesattached_list = filesattached.split(",")
				for each in filesattached_list:
					print int(each)
					file_to_attach = AttachedFiles.objects.get(pk=int(each))
					newobject.files.add(file_to_attach)
					newobject.save()
			return HttpResponseRedirect(reverse('index', ))
	else:
		form = FileResourceForm(instance=instance)
	return render_to_response('mediamanager/edit_fileresource.html', {'form': form,},context) 


def CreateFileResource(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = FileResourceForm(request.POST)
		if form.is_valid():
			newobject = form.save()
			filesattached = request.POST.get('filesattached',False)
			if filesattached:
				if filesattached[-1:] == ",":
					filesattached = filesattached[:-1]
				filesattached_list = filesattached.split(",")
				for each in filesattached_list:
					print int(each)
					file_to_attach = AttachedFiles.objects.get(pk=int(each))
					newobject.files.add(file_to_attach)
					newobject.save()
			return HttpResponseRedirect(reverse('index', ))
	else:
		form = FileResourceForm()
	return render_to_response('mediamanager/create_fileresource.html', {'form': form,},context) 




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

#Nothing here yet

#end exclusive keyword tags		
	
# Start of Pathway retreiving section.

	try:
		urlpathway = request.GET.get('pathway', False).lstrip("/")
		print urlpathway
	except:
		urlpathway = False
	urlpathwayfiltered_list = []
	if urlpathway:
		urlpathwaylist = urlpathway.split("/")
		if len(urlpathwaylist) > 0:
			objectslist=[]
			for each in urlpathwaylist:
				objectslist.append(AssoePathway.objects.get(pathway=each).pk)
			default_resource_list = default_resource_list.filter(pathway__in=objectslist).distinct()

		#if len(urlpathwaylist) > 0:
		#	for pathways in urlpathwaylist:
		#		for pathway in AssoePathway.objects.all():
		#			if str(pathway.pathway) not in urlpathwaylist:
		#				default_resource_list = default_resource_list.exclude(pathway=pathway.pk)
# END of Pathway retreiving section.


# Start of Level retreiving section.
	
	try:
		urllevel = request.GET.get('level', False).lstrip("/")
	except:
		urllevel = []
	urllevelfiltered_list = []
	if urllevel:
		urllevellist = urllevel.split("/")
		if len(urllevellist) > 0:
			objectslist=[]
			for each in urllevellist:
				objectslist.append(AssoeLevel.objects.get(level=each).pk)
			default_resource_list = default_resource_list.filter(level__in=objectslist).distinct()

# End of Level retreiving section.

# Start of AGE retreiving section.
#
#Rework this to match pathway becuase it retains it as a queryset object
	
	try:
		urlage = request.GET.get('age', False).lstrip("/")
	except:
		urlage = []
	urlagefiltered_list = []
	if urlage:
		urlagelist = urlage.split("/")
		if len(urlagelist) > 0:
			objectslist=[]
			for each in urlagelist:
				objectslist.append(AgeBracket.objects.get(agebracket=each).pk)
			default_resource_list = default_resource_list.filter(agebracket__in=objectslist).distinct()
# END of AGE retreiving section. request.GET.get('age', False) returns a value then default_resource_list is now a list filtered by agebracket.

	try:
		urlsubject = request.GET.get('subject', False).lstrip("/")
	except:
		urlsubject = []
	urlsubjectfiltered_list = []
	if urlsubject:
		urlsubjectlist = urlsubject.split("/")
		if len(urlsubjectlist) > 0:
			objectslist=[]
			for each in urlsubjectlist:
				objectslist.append(AssoeSubjects.objects.get(subject=each).pk)
			default_resource_list = default_resource_list.filter(subject__in=objectslist).distinct()
	
	default_resource_list = default_resource_list.order_by('-score').select_subclasses()
	tagcloud = []
	for each in default_resource_list[0:100]:
		for all in each.tags.all():
			tagcloud.append(all)
	print tagcloud


	#default_resource_list.sort(key=lambda x: x.score, reverse=True)
	
	paginator = Paginator(default_resource_list, 20)
	page = request.GET.get('page')
	try:
		paged_list = paginator.page(page)
	except PageNotAnInteger:
		paged_list = paginator.page(1)
	except EmptyPage:
		paged_list = paginator.page(paginator.num_pages)









	levels_list = AssoeLevel.objects.order_by('order')
	agebracket_list = AgeBracket.objects.order_by('order')
	pathway_list = AssoePathway.objects.order_by('order')
	subject_list = AssoeSubjects.objects.order_by('order')
	default_resource_list = list(set(default_resource_list))
	default_resource_list.sort(key=lambda x: x.score, reverse=True)

	
	context_dict = {'default_resource_list':paged_list,'levels_list':levels_list,'agebracket_list':agebracket_list,'pathway_list':pathway_list,'subject_list':subject_list,'tagcloud':tagcloud}
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


def fileresourceview(request, resource_slug):
	#
	#This view displays an individual resource
	#
	context_dict = {}
	default_resource = FileResource.objects.get(slug=resource_slug)
	default_resource.views = default_resource.views + 1
	default_resource.save()
	context_dict['default_resource'] = default_resource
	
	return render(request,'mediamanager/file_resource.html',context_dict)




def test(request):
	if request.method == 'POST':
		if request.FILES['file']:
			new_file = AttachedFiles(attachedfile=request.FILES['file'])
			new_file.save()
			id = new_file.pk
			return HttpResponse(json.dumps({'id': id}), content_type="application/json")
 	return render_to_response('mediamanager/test.html', context_instance=RequestContext(request))






