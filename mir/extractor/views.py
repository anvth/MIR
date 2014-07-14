from django.shortcuts import *
from extract_features import *
from csvtolibsvm import *
from svm_prediction import *
from django.http import *
from models import *
# Create your views here.

from mir.extractor.models import UploadForm,Upload
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.
def home(request):
    if request.method=="POST":
        img = UploadForm(request.POST, request.FILES)       
        if img.is_valid():
			img.save()
			uploaded_file_name=request.FILES['pic']
			print uploaded_file_name
			feats=extract_feature(uploaded_file_name) 
			#csvtolibsvm('1')
			#inst=predict()
			return HttpResponse("The Recognition system thinks it is <b>"+"</b> ")
			'''output = "onLoad=\"javascript:alert('The language is ');"
			print output+"\t valid form"
			form = UploadForm()
			return render_to_response('home.html', {'form': form,'output':output},context_instance=RequestContext(request))
			#return HttpResponseRedirect(reverse('/imageupload'))'''
			
    else:
        img=UploadForm()
    images=Upload.objects.all()
    return render(request,'home.html',{'form':img,'images':images})
