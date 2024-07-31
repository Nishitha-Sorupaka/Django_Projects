import os
import django

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_assignment.settings')
django.setup()

from testapp.models import MovieDB

def get_top_grossing_movies(year, top_n=5):
    # Get the top N movies for the specified year according to their gross
    top_grossing_movies = MovieDB.objects.filter(year=year).order_by('-gross')[:top_n]

    return top_grossing_movies

# Define the year and number of top movies you want to retrieve
year = 2023
top_n = 5

# Fetch and display the top grossing movies
top_movies = get_top_grossing_movies(year, top_n)
for movie in top_movies:
    print(f"Movie: {movie.movies}, Year: {movie.year}, Gross: {movie.gross}")
