from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from frontend.models import Machine_Learning_Models
from .forms import UploadFileForm

import csv

def index(request):
    algorithms_list = Machine_Learning_Models.objects.all()
    context = {'algorithms_list': algorithms_list}
    return render(request, 'frontend/index.html', context)

def model_info(request, model_name):
    algorithm = get_object_or_404(Machine_Learning_Models, slug=model_name)
    context = {'algorithm': algorithm}
    return render(request, 'frontend/models_info.html', context)


# Imaginary function to handle an uploaded file.
def handle_uploaded_file(f):
    data = [row for row in csv.reader(f.read().splitlines())]
    return data


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            name = request.FILES['file']
            data = handle_uploaded_file(name)
            return render_to_response('form/success.html', {'data': data, 'name': name})
    else:
        form = UploadFileForm()
    return render_to_response('form/upload.html', {'form': form},
            context_instance=RequestContext(request))
