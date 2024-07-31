from django.contrib import admin
from testapp.models import *
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','marks']
admin.site.register(Student, StudentAdmin)