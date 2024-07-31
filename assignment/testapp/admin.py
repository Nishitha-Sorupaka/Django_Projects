from django.contrib import admin
from testapp.models import *
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('MOVIES','YEAR','GENRE','RATING','ONE_LINE','STARS','VOTES','RunTime','Gross')

admin.site.register(Movie,MovieAdmin)

