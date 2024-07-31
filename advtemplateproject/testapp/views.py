from django.shortcuts import render
from testapp import *
# Create your views here.
def base_view(request):
    return render(request, 'testapp/base.html')
def movies_view(request):
    return render(request, 'testapp/movies.html')

def sports_view(request):
    return render(request, 'testapp/sports.html')

def politics_view(request):
    return render(request, 'testapp/politics.html')