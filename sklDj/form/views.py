from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import UploadFileForm

import csv
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
