from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hydjobs_info(request):
    s='<h1>Hyderabad Jobs Information</h1>'
    return HttpResponse(s)
def punejobs_info(request):
    s='<h1>Pune Jobs Information</h1>'
    return HttpResponse(s)
def bngjobs_info(request):
    s='<h1>Banglore Jobs Information</h1>'
    return HttpResponse(s)
def biharjobs_info(request):
    s='<h1>Bihar Jobs Information</h1>'
    return HttpResponse(s)