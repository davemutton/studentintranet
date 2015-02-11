from django.db import models
#create slugs for pages
from django.template.defaultfilters import slugify

#need zipfile to unpack archive
import zipfile, os,fnmatch

# Create your models here.

class DefaultPage(models.Model):
	title = models.CharField(max_length=100)
	created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	edited_date =  models.DateTimeField(auto_now_add=False,auto_now=True)
	parent_page = models.ForeignKey("self",blank=True, null=True)
	slug = models.SlugField(max_length=100,editable=False,blank=True)
	def __unicode__ (self): 
		return self.title
	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(DefaultPage, self).save(*args, **kwargs)

class Page(DefaultPage):
	body = models.TextField(blank=True)

class AdminPage(DefaultPage):
	body = models.TextField(blank=True)

class SubjectPage(DefaultPage):
	pass

class LearningObject(DefaultPage):
	archivefile = models.FileField(upload_to='static/learningobject/archivefiles/%Y/%m/%d')
	indexpath = models.CharField(max_length=254,editable=False)
	def unpackarchive(self):
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
	def findindex(self,path):

		print path
		for root, dirnames, filenames in os.walk(path):
			for filename in fnmatch.filter(filenames, 'index.ht*'):
				print filename
				self.indexpath = os.path.join(root, filename)
		print self.indexpath

	def save(self, *args, **kwargs):
		self.unpackarchive()
		super(LearningObject, self).save(*args, **kwargs)
