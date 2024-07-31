# testapp/management/commands/load_data.py
from django.core.management.base import BaseCommand
from testapp.models import *
import pandas as pd


class Command(BaseCommand):
    help = 'Load movies data from CSV file'

    def handle(self, *args, **kwargs):
        file_path = "E:\\Django_Projects\\assignment\\cleaned_movies.csv"  # actual CSV file path
        df = pd.read_csv(file_path)

        for _, row in df.iterrows():
            Movie.objects.create(
                MOVIES=row['MOVIES'],
                YEAR=row['YEAR'],
                GENRE=row['GENRE'],
                RATING=row['RATING'],
                ONE_LINE=row['ONE-LINE'],
                STARS=row['STARS'],
                VOTES=row['VOTES'],
                RunTime=row['RunTime'],
                Gross=row['Gross']
            )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
