from django.shortcuts import render
from testapp.models import *
# Create your views here.
def data_view(request):
    records = FilterModel.objects.all()
    return render(request, 'testapp/data.html', {'records': records})