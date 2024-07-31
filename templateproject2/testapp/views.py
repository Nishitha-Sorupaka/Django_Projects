from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def info_view(request):
    date = datetime.datetime.now()
    name = 'Django'
    prerequisite = 'Python'
    my_dict = {'date':date,'name':name,'prerequisite':prerequisite}
    return render(request,'testapp/results.html',my_dict)