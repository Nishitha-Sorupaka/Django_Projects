from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date = datetime.datetime.now()
    name = "Nishu"
    rollno = '101'
    marks = 98
    my_dict = {'date':date,'name':name,'rollno':rollno,'marks':marks}
    return render(request,'testapp/wish.html',my_dict)