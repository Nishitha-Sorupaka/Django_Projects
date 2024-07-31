# testapp/management/commands/load_data.py
from django.core.management.base import BaseCommand
from testapp.models import MovieDB
import pandas as pd

class Command(BaseCommand):
    help = 'Load movies data from CSV file'

    def handle(self, *args, **kwargs):
        file_path = "E:\\Django_Projects\\project_assignment\\cleaned_movies.csv"  # actual CSV file path
        df = pd.read_csv(file_path)

        for _, row in df.iterrows():
            MovieDB.objects.create(
                movies=row['MOVIES'],
                year=row['YEAR'],
                genre=row['GENRE'],
                rating=row['RATING'],
                oneLine=row['ONE-LINE'],
                stars=row['STARS'],
                votes=row['VOTES'],
                runTime=row['RunTime'],
                gross=row['Gross']
            )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
