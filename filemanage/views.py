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
	
	return JsonResponse({'filename': queriedfile.getfilename(),'filesize': queriedfile.getfilesize()})




def FileUpload(request):
	if request.method == 'OPTIONS':
		response = HttpResponse()
		response['allow'] = ','.join([allowed_methods])
		return response

	if request.method == 'POST':
		if request.FILES.get('file',False):
			new_file = AttachedFiles(attachedfile=request.FILES['file'])
			new_file.save()
			id = new_file.pk
			return JsonResponse({'id': id})
		print "but there was no file"
		return JsonResponse({'error': 'no file detected'})
	print "that was not POST"
 	return JsonResponse({'error': 'no POST request detected'})


    