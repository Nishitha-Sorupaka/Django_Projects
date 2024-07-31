#get_top_grossing_movies.py --->gets the top 5 movies according to gross for a particular year.
import os
import django
from django.core.management.base import BaseCommand
from testapp.models import MovieDB
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Get top 5 grossing movies for a particular year'

    def add_arguments(self, parser):
        parser.add_argument('year', type=int, help='Year for which to fetch top grossing movies')

    def handle(self, *args, **options):
        year = options['year']
        top_n = 5

        try:
            # Using Django ORM to filter, order, and limit the results
            top_grossing_movies = MovieDB.objects.filter(year=year).order_by('-gross')[:top_n]

            if not top_grossing_movies:
                self.stdout.write(self.style.WARNING(f'No movies found for the year {year}'))
                return

            self.stdout.write(self.style.SUCCESS(f'Top {top_n} grossing movies for the year {year}:'))
            for movie in top_grossing_movies:
                self.stdout.write(f"Movie: {movie.movies}, Year: {movie.year}, Gross: {movie.gross}")

        except ObjectDoesNotExist:
            self.stdout.write(self.style.ERROR(f'Error fetching data for the year {year}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An unexpected error occurred: {str(e)}'))
