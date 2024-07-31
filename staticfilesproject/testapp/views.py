from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def image_view(request):
    brands = {'b1':'KF','b2':'RC','b3':'boom'}
    return render(request,'testapp/results.html',context=brands)