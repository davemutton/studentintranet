from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context
from django.http import HttpResponseRedirect, HttpResponse
#required for create page
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from wiki.models import DefaultPage, Page, LearningObject
from wiki.forms import PageForm, LearningObjectForm
# Create your views here.


class createPage(CreateView):
	model = Page
	template_name = 'wiki/edit_page.html'
	def get_success_url(self):
		return reverse('index')
		
class createLearningobject(CreateView):
	model = LearningObject
	template_name = 'wiki/learningobject_form.html'
	def get_success_url(self):
		return reverse('index')

def index(request):
	context = RequestContext(request)
	defaultpages_list = DefaultPage.objects.order_by('edited_date')
	context_dict = {'defaultpages':defaultpages_list}
	return render_to_response('wiki/index.html', context_dict, context)

def defaultpageview(request, default_page_slug):
	context_dict = {}
	try:
		default_page = DefaultPage.objects.get(slug=default_page_slug)
		child_pages = DefaultPage.objects.filter(parent_page=default_page)
		print child_pages
		context_dict['default_page'] = default_page
		context_dict['child_pages'] = child_pages

	except:
		pass
	return render(request,'wiki/default_page.html',context_dict)



def page_form(request, parent_page_id):
	print 
	if request.method == 'GET':
		form = PageForm()
	else:
		form = PageForm(request.POST)
		if form.is_valid():
			content = form.cleaned_data['content']
			title = form.cleaned_data['title']
			parent_page = DefaultPage.objects.get(pk=parent_page_id)
			print parent_page_id
			print parent_page
			post = Page.objects.create(body=content,title=title,parent_page=parent_page)

			return HttpResponseRedirect(reverse('index', ))
	return render(request, 'wiki/page_form.html', {'form': form,})	


def learningobject_form(request, parent_page_id):
	print 
	if request.method == 'GET':
		form = LearningObjectForm()
	else:
		form = LearningObjectForm(request.POST, request.FILES)
		if form.is_valid():
			print request.FILES
			print request.FILES['archivefile']
			learningobject = request.FILES['archivefile']
			title = form.cleaned_data['title']
			parent_page = DefaultPage.objects.get(pk=parent_page_id)
			print parent_page_id
			print parent_page
			post = LearningObject.objects.create(archivefile=learningobject,title=title,parent_page=parent_page)

			return HttpResponseRedirect(reverse('index', ))
	return render(request, 'wiki/learningobject_form.html', {'form': form,})	