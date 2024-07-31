#models.py
from django.db import models
# Create your models here.
class MovieDB(models.Model):
    movies = models.CharField(max_length=300)
    year = models.IntegerField()
    genre = models.CharField(max_length=300)
    rating = models.FloatField()
    oneLine = models.TextField()
    stars = models.CharField(max_length=250)
    votes = models.CharField(max_length=250)
    runTime = models.FloatField()
    gross = models.CharField(max_length=250)
