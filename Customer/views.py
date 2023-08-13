from django.shortcuts import render
from .models import ServiceRequest
# Create your views here.

def index(request):
    return render(request, 'C:/Users/Pavan/Desktop/Bynry Task/gas_utility/templates/index.html')

def request_list(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'C:/Users/Pavan/Desktop/Bynry Task/gas_utility/templates/request_list.html', {'requests': requests})

def request_detail(request, request_id):
    request_obj = get_object_or_404(ServiceRequest, id=request_id)
    return render(request, 'C:/Users/Pavan/Desktop/Bynry Task/gas_utility/templates/request_detail.html', {'request_obj': request_obj})