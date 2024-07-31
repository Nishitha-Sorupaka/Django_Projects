from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from testapp.models import Company
from django.urls import reverse_lazy
# Create your views here.
class CompanyListView(ListView):
    model = Company
    #template file: company_list.html
    #context object name: company_list

class CompanyDetailView(DetailView):
    model = Company

class CompanyCreateView(CreateView):
    model = Company
    fields = '__all__'

class CompanyUpdateView(UpdateView):
    model = Company
    fields = '__all__'

class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('list')