from django.db import models

# Create your models here.
class Movie(models.Model):
    MOVIES = models.CharField(max_length=300)
    YEAR = models.IntegerField()
    GENRE = models.CharField(max_length=300)
    RATING = models.FloatField()
    ONELINE = models.TextField()
    STARS = models.CharField(max_length=250)
    VOTES = models.CharField(max_length=250)
    RunTime = models.FloatField()
    Gross = models.CharField(max_length=250)


    def __str__(self):
        return self.MOVIES