from django.shortcuts import render, render_to_response
from django.views.generic import CreateView
from mediamanager.models import LearningObject, FileResource, AttachedFiles, DefaultResource, AssoeLevel, AgeBracket, AssoePathway, AssoeSubjects
from forms import UploadFileForm
from django.http import HttpResponseRedirect
from mediamanager.forms import FileResourceForm, LearningObjectuploadform, LearningObjectuploadform2
from django.template import RequestContext
from django.core.urlresolvers import reverse
from taggit.models import Tag
import sys
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView
# Create your views here.
'''
def createLearningobject(request,learningobject_pk=False):
	if request.method == 'GET':
		if learningobject_pk:
			instance = LearningObject.objects.get( pk=learningobject_pk)
			form = LearningObjectuploadform(request.POST or None, request.FILES or None, instance=instance)
			form.base_fields['archivefile'].required = False
		else:
			form = LearningObjectuploadform()
	else:	
		form = LearningObjectuploadform(request.POST, request.FILES)
		if learningobject_pk:
			form.base_fields['archivefile'].required = False
		if form.is_valid():
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
'''
def createLearningobject(request,learningobject_pk=False):
	if request.method == 'POST':
		if learningobject_pk:
			instance = LearningObject.objects.get(pk=learningobject_pk)
			form = LearningObjectuploadform2(request.POST,request.FILES, instance=instance)
			if form.is_valid():
				form.save(instance)
		else:
			instance = None
			form = LearningObjectuploadform2(request.POST,request.FILES)
			if form.is_valid():
				form.save()
		

			return HttpResponseRedirect(reverse('index', ))
	else:
		if learningobject_pk:
			instance = LearningObject.objects.get( pk=learningobject_pk)
		else:
			instance = LearningObject()
		form = LearningObjectuploadform(instance=instance)
		form.base_fields['archivefile'].required = False
		print instance.pk
	return render_to_response('mediamanager/edit_learningobject.html', {'form': form,},context_instance=RequestContext(request)) 



class UpdateLearningObject(UpdateView):
	model = LearningObject
	template_name = 'mediamanager/edit_learningobject.html'
	def get_success_url(self):
		return reverse('index')



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
	

	try:
		urlpathway = request.GET.get('pathway', False).lstrip("/")
		print urlpathway
	except:
		urlpathway = False
	urlpathwayfiltered_list = []
	if urlpathway:
		urlpathwaylist = urlpathway.split("/")
		if len(urlpathwaylist) > 0:

			for pathways in urlpathwaylist:
				p = AssoePathway.objects.get(pathway=pathways)
				for pathway in AssoePathway.objects.all():
					if pathway not in urlpathwaylist:
						default_resource_list = default_resource_list.exclude(pathway=pathway.pk)


	try:
		urlage = request.GET.get('age', False).lstrip("/")
	except:
		urlage = False
	urlagefiltered_list = []
	if urlage:
		urlagelist = urlage.split("/")
		if len(urlagelist) > 0:
			for ages in urlagelist:
				p = AgeBracket.objects.get(agebracket=ages)
				default_resource_list = default_resource_list.filter(agebracket=p.pk)






			for objects in default_resource_list:
				for taggedage in objects.agebracket.all():
					for age in urlagelist:
						if age == str(taggedage):
							urlagefiltered_list.append(objects)
			default_resource_list = urlagefiltered_list
			default_resource_list = list(set(default_resource_list))
			default_resource_list.sort(key=lambda x: x.score, reverse=True)

	try:
		urllevel = request.GET.get('level', False).lstrip("/")
	except:
		urllevel = []
	urllevelfiltered_list = []
	if urllevel:
		urllevellist = urllevel.split("/")
		if len(urllevellist) > 0:
			print urllevellist
			for objects in default_resource_list:
				for taggedlevel in objects.level.all():
					for level in urllevellist:
						if level == str(taggedlevel):
							urllevelfiltered_list.append(objects)
			default_resource_list = urllevelfiltered_list
			default_resource_list = list(set(default_resource_list))
			default_resource_list.sort(key=lambda x: x.score, reverse=True)
	
	try:
		urlsubject = request.GET.get('subject', False).lstrip("/")
	except:
		urlsubject = [] 
	urlsubjectfiltered_list = []
	if urlsubject:
		urlsubjectlist = urlsubject.split("/")
		if len(urlsubjectlist) > 0:
			print urlsubjectlist
			for objects in default_resource_list:
				for taggedsubject in objects.subject.all():
					for subject in urlsubjectlist:
						if subject == str(taggedsubject):
							urlsubjectfiltered_list.append(objects)
			default_resource_list = urlsubjectfiltered_list
			default_resource_list = list(set(default_resource_list))
		
		default_resource_list.sort(key=lambda x: x.score, reverse=True)
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

	
	context_dict = {'default_resource_list':paged_list,'levels_list':levels_list,'agebracket_list':agebracket_list,'pathway_list':pathway_list,'subject_list':subject_list}
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