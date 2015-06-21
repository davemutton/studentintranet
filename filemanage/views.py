from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import JsonResponse, HttpResponse

from django.conf import settings
from filemanage.models import AttachedFiles
from mediamanager.models import FileResource
import os.path
import mimetypes
# Create your views here.

def index(request):
	context = RequestContext(request)
	return render_to_response('filemanage/index.html', context)

def QuerySingleFile(request,pk):
	queriedfile = AttachedFiles.objects.get(pk=pk)
	filepath = str(queriedfile.attachedfile)
	return JsonResponse({'path':filepath,'filename': queriedfile.getfilename(),'icon':queriedfile.icon,'filesize': queriedfile.getfilesize()})

def ReturnAttachedFiles(request,pk):
	queriedfile = FileResource.objects.get(pk=pk)
	for each in queriedfile.files.all():
		print each
	return JsonResponse({'files':str(queriedfile.files.all())})

def DeleteFile(request,pk):
	AttachedFiles.objects.get(pk=pk).delete()
	return JsonResponse({'success': True})

def FileUpload(request):
	if request.method == 'OPTIONS':
		response = HttpResponse()
		response['allow'] = ','.join([allowed_methods])
		return response

	if request.method == 'POST':
		if request.FILES.get('file',False):
			queriedfile = AttachedFiles(attachedfile=request.FILES['file'])
			queriedfile.save()
			id = queriedfile.pk
			filepath = str(queriedfile.attachedfile)
			return JsonResponse({'path':filepath, 'id': id,'filename': queriedfile.getfilename(),'icon':queriedfile.icon,'filesize': queriedfile.getfilesize()})
		print "but there was no file"
		return JsonResponse({'error': 'no file detected'})
	print "that was not POST"
 	return JsonResponse({'error': 'no POST request detected'})

def DownloadFile(request,pk):
	queriedfile = AttachedFiles.objects.get(pk=pk)
	mimetypes.init()


	file_url = str(queriedfile.attachedfile)
	print file_url
	file_path = settings.MEDIA_ROOT + '/' + file_url
	fsock = open(file_path,"r")
	#file = fsock.read()
	#fsock = open(file_path,"r").read()
	file_name = os.path.basename(file_path)
	file_size = os.path.getsize(file_path)
	print "file size is: " + str(file_size)
	mime_type_guess = mimetypes.guess_type(file_name)
	if mime_type_guess is not None:
		response = HttpResponse(fsock, content_type=mime_type_guess[0])
	response['Content-Disposition'] = 'attachment; filename=' + file_name            

	return response
