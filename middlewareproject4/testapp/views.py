from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page_view(request):
    print('This response is from view function')
    return HttpResponse("<h1>This response is from view function</h1>")
