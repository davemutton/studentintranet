from django.db import models
from hurry.filesize import size
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

import os
from PIL import Image



# Create your models here.
class AttachedFiles(models.Model):
	#
	#This class creates stores attached files so they can be attached to other objects
	#
	attachedfile = models.FileField(upload_to='attachedfiles/%Y/%m/%d')
	icon = models.CharField(max_length=254,editable=False,blank=True)
	thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/%d',blank=True)
	def __unicode__ (self): 
		return self.getfilename()
	def getfilename(self):
		file = self.attachedfile
		filename = os.path.basename(file.name)
		if len(filename) > 15:
			filename = filename[:8] + "..." +filename[-5:]
		return filename
	def getfullfilename(self):
		file = self.attachedfile
		filename = os.path.basename(file.name)
		return filename
	
	def getfilesize(self):
		file = self.attachedfile
		return size(file.size)


	def seticon(self):
		extension = os.path.basename(self.attachedfile.name).split('.')[1]
		image_formats = ["jpg","jpeg","png"]
		if extension.lower() in image_formats:
			from PIL import Image
			from cStringIO import StringIO
			from django.core.files.uploadedfile import SimpleUploadedFile

			# Set our max thumbnail size in a tuple (max width, max height)
			THUMBNAIL_SIZE = (200, 200)

			# Open original photo which we want to thumbnail using PIL's Image
			# object
			image = Image.open(self.attachedfile)

			# Convert to RGB if necessary
			# Thanks to Limodou on DjangoSnippets.org
			# http://www.djangosnippets.org/snippets/20/
			if image.mode not in ('L', 'RGB'):
			    image = image.convert('RGB')

			# We use our PIL Image object to create the thumbnail, which already
			# has a thumbnail() convenience method that contrains proportions.
			# Additionally, we use Image.ANTIALIAS to make the image look better.
			# Without antialiasing the image pattern artifacts may result.
			image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

			# Save the thumbnail
			temp_handle = StringIO()
			image.save(temp_handle, 'png')
			temp_handle.seek(0)

			# Save to the thumbnail field
			suf = SimpleUploadedFile(os.path.split(self.attachedfile.path)[-1],
				temp_handle.read(), content_type='image/png')
			self.thumbnail.save(suf.name+'.png', suf, save=False)
			self.icon = "/media/"+str(self.thumbnail)
		else:			


			icons ={'doc': '/static/images/icons/word.png', 
					'docx': '/static/images/icons/word.png',
					'pdf': '/static/images/icons/pdf.png',
					'psd': '/static/images/icons/psd.png',
					'xls': '/static/images/icons/excel.png',
					'xlsx': '/static/images/icons/excel.png',
					'csv': '/static/images/icons/excel.png',
					'ppt': '/static/images/icons/powerpoint.png',
					'pptx': '/static/images/icons/powerpoint.png',
					'zip': '/static/images/icons/powerpoint.zip',
					}

			try:
				self.icon = icons[extension]
			except:
				self.icon = '/static/images/icons/blank.png'
		print extension
		print self.icon
		return

	def save(self, *args, **kwargs):
		if self.pk is None:
			self.seticon()
		super(AttachedFiles, self).save(*args, **kwargs)