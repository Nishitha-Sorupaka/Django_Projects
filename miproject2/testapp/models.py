from django.db import models

# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset().order_by('-eno')
        return qs
    def get_emp_sal_range(self,minsal,maxsal):
        qs = super().get_queryset().filter(esal__range(minsal,maxsal))
        return qs
    def get_emp_sorted_by(self,param):
        qs = super().get_queryset().order_by(param)
        return qs
class CustomManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__gte=18000)
class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__lte=12000)
class CustomManager3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('eno')

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=120)
    #objects = CustomManager()
    objects = CustomManager1()

class ProxyManager(Employee):
    objects = CustomManager2()
    class Meta:
        proxy = True

class ProxyEmployee2(Employee):
    objects = CustomManager3()
    class Meta:
        proxy = True


