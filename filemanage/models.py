from django.db import models
from hurry.filesize import size
import os

# Create your models here.
class AttachedFiles(models.Model):
	#
	#This class creates stores attached files so they can be attached to other objects
	#
	attachedfile = models.FileField(upload_to='attachedfiles/%Y/%m/%d')
	icon = models.CharField(max_length=254,editable=False,blank=True)
	def getfilename(self):
		file = self.attachedfile
		return os.path.basename(file.name)
	def getfilesize(self):
		file = self.attachedfile
		return size(file.size)
	def seticon(self):
		extension = os.path.basename(self.attachedfile.name).split('.')[1]
		icons ={'doc': '/static/images/icons/microsoft-word.png', 
				'docx': '/static/images/icons/microsoft-word.png'
				}
		try:
			self.icon = icons[extension]
		except:
			self.icon = '/static/images/icons/blank.png'
		print extension
		print self.icon
		return

	def save(self, *args, **kwargs):
		self.seticon()
		super(AttachedFiles, self).save(*args, **kwargs)