#get_top_rated_movies.py --->gets the top 10 movies according to rating for a particular year
import os
import django
from django.core.management.base import BaseCommand
from testapp.models import MovieDB
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Get top 10 movies according to rating for a particular year'

    def add_arguments(self, parser):
        parser.add_argument('year', type=int, help='Year for which to fetch top rated movies')

    def handle(self, *args, **options):
        year = options['year']
        top_n = 10

        try:
            # Using Django ORM to filter, order, and limit the results
            top_rated_movies = MovieDB.objects.filter(year=year).order_by('-rating')[:top_n]

            if not top_rated_movies:
                self.stdout.write(self.style.WARNING(f'No movies found for the year {year}'))
                return

            self.stdout.write(self.style.SUCCESS(f'Top {top_n} rated movies for the year {year}:'))
            for movie in top_rated_movies:
                self.stdout.write(f"Movie: {movie.movies}, Year: {movie.year}, Rating: {movie.rating}")

        except ObjectDoesNotExist:
            self.stdout.write(self.style.ERROR(f'Error fetching data for the year {year}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An unexpected error occurred: {str(e)}'))
