from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish1(request):
    s="<h1>Hello from first application</h1>"
    return HttpResponse(s)
