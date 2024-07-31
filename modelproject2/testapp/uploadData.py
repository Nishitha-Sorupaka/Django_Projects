# In a file named import_csv.py within a management/commands directory inside your app
from django.core.management.base import BaseCommand
import csv
from testapp.models import MovieDB # Import your model here

class Command(BaseCommand):
    help = 'Imports a CSV file into MyModel table'

    def add_arguments(self, parser):
        parser.add_argument('cleaned_movies.csv', type=str, help="E:\\Django_Projects\\project_assignment\\cleaned_movies.csv")

    def handle(self, *args, **kwargs):
        csv_file = kwargs['cleaned_movies.csv']

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                _, created = MovieDB.objects.get_or_create(
                    movies=row[0],
                    year=row[1],
                    genre=row[2],
                    rating=row[3],
                    oneLine=row[4],
                    stars=row[5],
                    votes=row[6],
                    runTime=row[7],
                    gross=row[8],

                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully imported row: {row}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Skipped duplicate row: {row}'))