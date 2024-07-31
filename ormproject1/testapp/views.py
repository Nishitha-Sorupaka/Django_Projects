from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q
from django.db.models import Avg,Max,Min,Sum,Count
from django.db.models.functions import Lower
# Create your views here.
def retrieve_view(request):
    #emp_list = Employee.objects.all()
    #emp_list = Employee.objects.filter(esal__gt=15000)
    #emp_list = Employee.objects.filter(esal__gte=15000)
    #emp_list = Employee.objects.filter(esal__lt=15000)
    #emp_list = Employee.objects.filter(esal__lte=15000)
    #emp_list = Employee.objects.filter(id__in=[1,3,5])
    #emp_list = Employee.objects.filter(ename__startswith='S')
    #emp_list = Employee.objects.filter(ename__endswith='y')
    #emp_list = Employee.objects.filter(esal__range=[12000,14000])
    #emp_list = Employee.objects.filter(ename__startswith='S') | Employee.objects.filter(esal__lt=15000)
    #emp_list = Employee.objects.filter(Q(ename__startswith='S') | Q(esal__lt=12000))
    #emp_list = Employee.objects.filter(ename__startswith='S') & Employee.objects.filter(esal__gt=15000)
    #emp_list = Employee.objects.filter(Q(ename__startswith='D') & Q(esal__gt=13000))
    #emp_list = Employee.objects.filter(ename__startswith='A', esal__gt=12000)
    #emp_list = Employee.objects.exclude(ename__startswith='M')
    #emp_list = Employee.objects.filter(~Q(ename__startswith='A'))
    #emp_list = Employee.objects.all().values_list('ename','esal')
    #emp_list = Employee.objects.all().values('ename','esal')
    #emp_list = Employee.objects.all().only('ename', 'esal')
    #emp_list = Employee.objects.all().order_by('eno')
    #emp_list = Employee.objects.all().order_by('-eno')
    #emp_list = Employee.objects.all().order_by('ename')
    #emp_list = Employee.objects.all().order_by('-ename')
    #emp_list = Employee.objects.all().order_by(Lower('ename'))
    emp_list=Employee.objects.all().order_by('esal')
    print(type(emp_list))
    return render(request, 'testapp/index.html', {'emp_list': emp_list})
    #return render(request, 'testapp/specificcolumns.html', {'emp_list': emp_list})
    #return render(request, 'testapp/values.html', {'emp_list': emp_list})
    #return render(request, 'testapp/only.html', {'emp_list': emp_list})

def aggregate_view(request):
    print(request.user)
    avg = Employee.objects.all().aggregate(Avg('esal'))
    max = Employee.objects.all().aggregate(Max('esal'))
    min = Employee.objects.all().aggregate(Min('esal'))
    sum = Employee.objects.all().aggregate(Sum('esal'))
    count = Employee.objects.all().aggregate(Count('esal'))
    my_dict = {'avg': avg['esal__avg'], 'max': max['esal__max'], 'min': min['esal__min'], 'sum': sum['esal__sum'], 'count': count['esal__count']}
    return render(request, 'testapp/aggregate.html', my_dict)