#views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import MovieDB

def top_gross_movies(request, year):
    movies = MovieDB.objects.filter(year=year).order_by('-gross')[:10]
    data = list(movies.values())
    return JsonResponse(data, safe=False)

def top_voted_movies(request):
    movies = MovieDB.objects.order_by('-votes')[:5]
    data = list(movies.values())
    return JsonResponse(data, safe=False)

def top_rated_movies(request, year):
    movies = MovieDB.objects.filter(year=year).order_by('-rating')[:10]
    data = list(movies.values())
    return JsonResponse(data, safe=False)