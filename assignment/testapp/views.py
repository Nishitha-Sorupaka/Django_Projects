from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Movie
from .serializer import MovieSerializer


def get(self, request):
    # Use the Movie model instead of React
    movies = Movie.objects.all()
    for movie in movies:
        print(f"Movie: {movie.MOVIES}")
        print(f"Year: {movie.YEAR}")
        print(f"Genre: {movie.GENRE}")
        print(f"Rating: {movie.RATING}")
        print(f"One Line: {movie.ONE_LINE}")
        print(f"Stars: {movie.STARS}")
        print(f"Votes: {movie.VOTES}")
        print(f"Runtime: {movie.RunTime}")
        print(f"Gross: {movie.Gross}")
        print("-" * 20)  # Just for separation
        output = [
            {
                #'movies': movie.movies,
                'year': movie.year,
                'genre': movie.genre,
                'rating': movie.rating,
                'one_line': movie.one-line,
                'stars': movie.stars,
                'votes': movie.votes,
                'runtime': movie.runtime,
                'gross': movie.gross
            }
            for movie in movies
        ]
        return Response(output)



def top_grossing_movies(request, year):
    try:
        top_movies = Movie.objects.filter(year=year).order_by('-gross')[:5]
        if not top_movies:
            return JsonResponse({'error': 'No movies found for the specified year'}, status=404)

        data = {
            'movies': list(
                top_movies.values('movies', 'year', 'genre', 'rating', 'one_line', 'stars', 'votes', 'runtime', 'gross')
            )
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def top_voted_movies(request):
    try:
        top_movies = Movie.objects.order_by('-votes')[:5]
        if not top_movies:
            return JsonResponse({'error': 'No movies found'}, status=404)

        data = {
            'movies': list(
                top_movies.values('movies', 'year', 'genre', 'rating', 'one_line', 'stars', 'votes', 'runtime', 'gross')
            )
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def top_rated_movies(request, year):
    try:
        top_movies = Movie.objects.filter(year=year).order_by('-rating')[:10]
        if not top_movies:
            return JsonResponse({'error': 'No movies found for the specified year'}, status=404)

        data = {
            'movies': list(
                top_movies.values('movies', 'year', 'genre', 'rating', 'one_line', 'stars', 'votes', 'runtime', 'gross')
            )
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
