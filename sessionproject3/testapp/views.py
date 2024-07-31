from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')


def age_view(request):
    print(request.COOKIES)
    name = request.GET['name']
    response = render(request,'testapp/age.html',{'name':name})
    response.set_cookie('name',name)
    return response

def gf_view(request):
    print(request.COOKIES)
    name = request.COOKIES['name']
    age = request.GET['age']
    response = render(request,'testapp/gf.html',{'name':name})
    response.set_cookie('age',age)
    return response

def results_view(request):
    print(request.COOKIES)
    gf = request.GET['gf']
    age = request.COOKIES['age']
    name = request.COOKIES['name']
    response = render(request,'testapp/results.html',{'gf':gf,'age':age,'name':name})
    return response