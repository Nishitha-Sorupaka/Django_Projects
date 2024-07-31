# djangoproj/reactapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie
from django.views.generic import TemplateView
'''
def index(request):
    # Your view logic for the index page
    return render(request, 'index.html')'''
class IndexView(TemplateView):
    template_name = 'index.html'
def top_gross_movies(request, year):
    movies = Movie.objects.filter(YEAR=year).order_by('-Gross')[:5]
    data = list(movies.values())
    return JsonResponse(data, safe=False)

def top_voted_movies(request):
    movies = Movie.objects.order_by('-VOTES')[:5]
    data = list(movies.values())
    return JsonResponse(data, safe=False)

def top_rated_movies(request, year):
    movies = Movie.objects.filter(YEAR=year).order_by('-RATING')[:10]
    data = list(movies.values())
    return JsonResponse(data, safe=False)