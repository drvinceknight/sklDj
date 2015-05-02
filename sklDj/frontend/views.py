from django.shortcuts import get_object_or_404, render
from frontend.models import Machine_Learning_Models

def index(request):
    algorithms_list = Machine_Learning_Models.objects.all()
    context = {'algorithms_list': algorithms_list}
    return render(request, 'frontend/index.html', context)

def model_info(request, model_name):
    algorithm = get_object_or_404(Machine_Learning_Models, slug=model_name)
    context = {'algorithm': algorithm}
    return render(request, 'frontend/models_info.html', context)
