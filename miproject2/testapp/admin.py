from django.contrib import admin
from testapp.models import *
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr']

class ProxyEmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(ProxyManager,ProxyEmployeeAdmin)
admin.site.register(ProxyEmployee2,ProxyEmployeeAdmin)