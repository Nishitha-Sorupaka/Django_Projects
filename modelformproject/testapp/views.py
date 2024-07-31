from django.shortcuts import render
from testapp.forms import *
# Create your views here.
def student_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Record inserted into database successfully")
    form = StudentForm()
    return render(request, 'testapp/studentform.html', {'form': form})