from django.contrib import admin
from testapp.models import *
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movies','year','genre','rating','oneLine','stars','votes','runTime','gross')

admin.site.register(MovieDB,MovieAdmin)

