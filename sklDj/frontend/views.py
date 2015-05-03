from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from frontend.models import Machine_Learning_Models
from .forms import UploadFileForm

import csv
#import matplotlib.pyplot as plt, mpld3
#from sklearn.linear_model import LinearRegression

from implementations import *

def index(request):
    algorithms_list = Machine_Learning_Models.objects.all()
    form = UploadFileForm()
    context = {'algorithms_list': algorithms_list, 'form': form}
    return render_to_response('frontend/index.html', context,
            context_instance=RequestContext(request))

def model_info(request, model_name):
    algorithm = get_object_or_404(Machine_Learning_Models, slug=model_name)
    context = {'algorithm': algorithm}
    return render(request, 'frontend/models_info.html', context)

def model_upload(request, model_name):
    # algorithms_list = Machine_Learning_Models.objects.all()
    algorithm = get_object_or_404(Machine_Learning_Models, slug=model_name)
    # Assuming request.method is always POST
    #form = UploadFileForm(request.POST, request.FILES)

    #if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        name = request.FILES['file']
        data = read_data(name)
        try:
            implementation = implementations_dict[model_name](data)
        except KeyError:
            return render_to_response('frontend/notimplemented.html', {'algorithm': algorithm})
        fig_html, coeff, intercept = implementation.run()
        return render_to_response('frontend/results.html', {'fig_html': fig_html,
            'algorithm': algorithm, 'name':name, 'coeff': coeff})
    #else:
        #form = UploadFileForm()
    #context = {'algorithms_list': algorithms_list, 'form':form}
    #return render_to_response('frontend/index.html', context,
            #context_instance=RequestContext(request))

##############
def read_data(f):
    data = [[eval(k) for k in row] for row in csv.reader(f.read().splitlines())]
    return data
