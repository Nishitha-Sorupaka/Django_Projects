from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    s="<h1><i>Hello Welcome to Django Project...</i></h1>"
    return HttpResponse(s)