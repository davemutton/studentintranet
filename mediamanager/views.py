from django.shortcuts import render
from django.views.generic import CreateView
from mediamanager.models import LearningObject
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
	fields =['title','tags','pathway','level','agebracket']