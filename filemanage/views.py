from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import JsonResponse
from filemanage.models import AttachedFiles
# Create your views here.

def index(request):
	context = RequestContext(request)
	return render_to_response('filemanage/index.html', context)

def QuerySingleFile(request,pk):
	queriedfile = AttachedFiles.objects.get(pk=pk)
	filepath = str(queriedfile.attachedfile)

	return JsonResponse({'path':filepath,'filename': queriedfile.getfilename(),'icon':queriedfile.icon,'filesize': queriedfile.getfilesize()})




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


    