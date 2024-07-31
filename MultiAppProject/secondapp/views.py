from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish2(request):
    s="<h1>Hello from second application</h1>"
    return HttpResponse(s)