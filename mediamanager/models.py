from django.db import models
#create slugs for pages
from django.template.defaultfilters import slugify
from django.conf import settings
from django.http import HttpResponse

from taggit_autosuggest.managers import TaggableManager
from updown.fields import RatingField
from taggit.models import Tag
from model_utils.managers import InheritanceManager
from filemanage.models import AttachedFiles
#need zipfile to unpack archive
import os,fnmatch, io
from StringIO import StringIO 
from zipfile import ZipFile


 
# Create your models here.

#########################################################
#
#
#Classification models
#
#
#########################################################
class AssoeLevel(models.Model):
	#
	# Used for content tagging(what Level is the object suitable for?)
	#
	level = models.CharField(max_length=25)
	order = models.IntegerField()
	def __unicode__ (self): 
		return self.level	

class AssoePathway(models.Model):
	#
	# Used for content tagging(what pathway is the object suitable for?)
	#
	pathway = models.CharField(max_length=1)
	order = models.IntegerField()
	def __unicode__ (self): 
		return self.pathway

class AgeBracket(models.Model):
	#
	# Used for content tagging (what age is the object suitable for?)
	#
	agebracket = models.CharField(max_length=25)
	order = models.IntegerField()
	def __unicode__ (self): 
		return self.agebracket

class AssoeSubjects(models.Model):
	#
	# Used for content tagging(what subject is the object suitable for?)
	#
	subject = models.CharField(max_length=55)
	order = models.IntegerField()
	slug = models.SlugField(max_length=100,editable=False,blank=True)
	def __unicode__ (self): 
		return self.subject
	def save(self, *args, **kwargs):
		#if not self.id:
		self.slug = slugify(self.subject)
		super(AssoeSubjects, self).save(*args, **kwargs)

#########################################################
#
#
#object storage models
#
#
#########################################################


class DefaultResource(models.Model):
	#
	# This class is the parent class for all resources in the media manager
	#
	objects = InheritanceManager()
	title = models.CharField(max_length=100)
	created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	edited_date =  models.DateTimeField(auto_now_add=False,auto_now=True)
	level = models.ManyToManyField(AssoeLevel)
	agebracket= models.ManyToManyField(AgeBracket)
	pathway= models.ManyToManyField(AssoePathway)
	tags = TaggableManager()
	slug = models.SlugField(max_length=100,editable=False,blank=True)
	updownvotes = RatingField(can_change_vote=True)
	views = models.DecimalField(max_digits=20,decimal_places=2,default=0,blank=True)
	score = models.DecimalField(max_digits=20,decimal_places=4,default=0,blank=True)
	icon = models.CharField(max_length=254,editable=False,blank=True)
	subject = models.ManyToManyField(AssoeSubjects)
	description = models.TextField(blank=True)


	def calculate_score(self):
		score = float(self.updownvotes.likes) - float(self.updownvotes.dislikes)
		score = score + (float(self.views)**(float(1)/float(2)))
		self.score = score
		rounded_score = int(round(self.score))
		if rounded_score < -1:
			return -1
		else:
			return rounded_score

	def __unicode__ (self): 
		return self.title

	def save(self, *args, **kwargs):
		self.calculate_score()
		if not self.id:
			self.slug = slugify(self.title)
		super(DefaultResource, self).save(*args, **kwargs)


class VideoResource(DefaultResource):
	videofile = models.FileField(upload_to='videofile/%Y/%m/%d')
	def save(self, *args, **kwargs):
		self.icon = "/static/images/icons/video.png"
		super(VideoResource, self).save(*args, **kwargs)



class UrlResource(DefaultResource):
	#
	#This class creates a object to store URLS
	#
	url = models.URLField(max_length=400)
	def __unicode__ (self): 
		return self.title

class FileResource(DefaultResource):
	#
	#This class creates a object to store collections attached file objects
	#
	files = models.ManyToManyField(AttachedFiles, blank=True,related_name="files")
	zipfile = models.FileField(upload_to='zipfilesofattachedfiles/%Y/%m/%d', blank=True)
	def __unicode__ (self): 
		return self.title
	def createzip(self):
		zip_filename =self.slug+".zip"
		list_of_files = self.files.all()
		print list_of_files
		filenames =[]
		for each in list_of_files:
			filenames.append(settings.MEDIA_ROOT + '/' + str(each.attachedfile))
		in_memory2 = StringIO()
		filelocationinmedia = '/' + "temp/" + str(self.slug)+'.zip'
		filelocation = settings.MEDIA_ROOT + filelocationinmedia
		zip = ZipFile(filelocation, "w")
		for fpath in filenames:
			zip.write(fpath,os.path.basename(fpath))
		for filez in zip.filelist:  
			filez.create_system = 0
		zip.close()
		print "bleh"
		self.zipfile.name = filelocationinmedia
		self.save()
		return "done"


			

	def save(self, *args, **kwargs):
		if self.pk:
			if not self.zipfile:
				self.createzip()
		self.icon = "/static/images/icons/folder.png"
		super(FileResource, self).save(*args, **kwargs)




class LearningObject(DefaultResource):
	archivefile = models.FileField(upload_to='static/learningobject/archivefiles/%Y/%m/%d')
	indexpath = models.CharField(max_length=254,editable=False,blank=True)
	def unpackarchive(self):
		if not self.pk:
			if self.archivefile:
				archive = self.archivefile
				filename = os.path.basename(str(archive))
				folder = str(filename).split(".")[0]
				print folder
				index_found = "False"
				with zipfile.ZipFile(archive,"r") as z:
					for each in z.namelist():
						if each == "index.html" or each == "index.htm":
							index_found = "True"
						else:
							pass
					if not index_found:
						print "zip file does not contain a valid index.html file"
					else:
						path = os.path.join("static","learningobject","unpackedarchives",folder)
						z.extractall(path)
						self.findindex(path)
		else:
			pass
	def findindex(self,path):

		print path
		for root, dirnames, filenames in os.walk(path):
			for filename in fnmatch.filter(filenames, 'index.ht*'):
				print filename
				self.indexpath = os.path.join(root, filename)
		print self.indexpath

	def save(self, *args, **kwargs):
		self.icon = "/static/images/icons/box.png"
		self.unpackarchive()
		super(LearningObject, self).save(*args, **kwargs)
