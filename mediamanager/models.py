from django.db import models
#create slugs for pages
from django.template.defaultfilters import slugify
from taggit_autosuggest.managers import TaggableManager
from updown.fields import RatingField
from taggit.models import Tag
from model_utils.managers import InheritanceManager
#need zipfile to unpack archive
import zipfile, os,fnmatch

 
# Create your models here.


class AssoeLevel(models.Model):
	#
	# Used for content tagging
	#
	level = models.CharField(max_length=25)
	order = models.IntegerField()
	def __unicode__ (self): 
		return self.level	

class AssoePathway(models.Model):
	#
	# Used for content tagging
	#
	pathway = models.CharField(max_length=1)
	order = models.IntegerField()
	def __unicode__ (self): 
		return self.pathway

class AgeBracket(models.Model):
	#
	# Used for content tagging
	#
	agebracket = models.CharField(max_length=25)
	order = models.IntegerField()
	def __unicode__ (self): 
		return self.agebracket

class AssoeSubjects(models.Model):
	#
	# Used for content tagging
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

	#def return_tags(self):
	#	taglist = self.tags.names()
	#	return taglist

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

class FileResource(DefaultResource):
	#
	#This class creates a object to store collections attached file objects
	#
	def __unicode__ (self): 
		return self.title

class UrlResource(DefaultResource):
	#
	#This class creates a object to store URLS
	#
	url = models.URLField(max_length=400)
	def __unicode__ (self): 
		return self.title


class AttachedFiles(models.Model):
	#
	#This class creates stores attached files so they can be attached to other objects
	#
	created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	attachedfiles = models.FileField(upload_to='static/attachedfiles/%Y/%m/%d')
	fileresource =models.ForeignKey(FileResource,blank=True, null=True) 
	def __unicode__ (self): 
		return self.attachedfiles


class LearningObject(DefaultResource):
	archivefile = models.FileField(upload_to='static/learningobject/archivefiles/%Y/%m/%d')
	indexpath = models.CharField(max_length=254,editable=False,blank=True)
	description = models.TextField(blank=True)
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
