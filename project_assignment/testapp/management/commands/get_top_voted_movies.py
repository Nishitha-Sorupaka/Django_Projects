#get_top_voted_movies.py--->gets top 5 movies of all time according to votes
import os
import django
from django.core.management.base import BaseCommand
from testapp.models import MovieDB
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Get top 5 movies or series of all time according to votes'

    def handle(self, *args, **options):
        top_n = 5

        try:
            # Using Django ORM to order and limit the results
            top_voted_movies = MovieDB.objects.order_by('-votes')[:top_n]

            if not top_voted_movies:
                self.stdout.write(self.style.WARNING('No movies or series found'))
                return

            self.stdout.write(self.style.SUCCESS(f'Top {top_n} movies or series of all time according to votes:'))
            for movie in top_voted_movies:
                self.stdout.write(f"Movie: {movie.movies}, Votes: {movie.votes}")

        except ObjectDoesNotExist:
            self.stdout.write(self.style.ERROR('Error fetching data'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An unexpected error occurred: {str(e)}'))
