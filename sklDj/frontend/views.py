from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from frontend.models import Machine_Learning_Models
from .forms import UploadFileForm

import csv
import matplotlib.pyplot as plt, mpld3
from sklearn.linear_model import LinearRegression

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
    algorithms_list = Machine_Learning_Models.objects.all()
    algorithm = get_object_or_404(Machine_Learning_Models, slug=model_name)
    # Assuming request.method is always POST
    #form = UploadFileForm(request.POST, request.FILES)

    #if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        name = request.FILES['file']
        fig_html = plot(name)
        return render_to_response('frontend/results.html', {'fig_html': fig_html,
            'algorithm': algorithm, 'name':name})
    #else:
        #form = UploadFileForm()
    #context = {'algorithms_list': algorithms_list, 'form':form}
    #return render_to_response('frontend/index.html', context,
            #context_instance=RequestContext(request))

# Imaginary function to handle an uploaded file.
def handle_uploaded_file(f):
    data = [row for row in csv.reader(f.read().splitlines())]
    return data


##############


# Imaginary function to handle an uploaded file.
def plot(f):
    data = [[eval(k) for k in row] for row in csv.reader(f.read().splitlines())]
    x = [[row[0]] for row in data]
    y = [row[1] for row in data]

    algorithm = LinearRegression()
    algorithm.fit(x,y)


    m = algorithm.coef_
    b = algorithm.intercept_
    fig = plt.figure()
    plt.scatter(x, y)
    plt.plot([min(x)[0],max(x)[0]], [m*min(x)[0] + b, m*max(x)[0] + b])
    fig_html = mpld3.fig_to_html(fig) # When we have local mpld3 libraries we will need to tweak this
    return fig_html
