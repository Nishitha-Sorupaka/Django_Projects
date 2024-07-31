from django.contrib import admin
from reactapp.models import *
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('MOVIES','YEAR','GENRE','RATING','ONELINE','STARS','VOTES','RunTime','Gross')

admin.site.register(Movie,MovieAdmin)

