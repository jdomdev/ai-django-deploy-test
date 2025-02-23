from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Company
from .forms import CompanyForm

class CompanyListView(ListView):
    model = Company
    template_name = 'api/company_list.html'
    context_object_name = 'companies'

class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'api/company_form.html'
    success_url = '/companies/'

class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'api/company_form.html'
    success_url = '/companies/'

class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'api/company_confirm_delete.html'
    success_url = '/companies/'

# Repite para User, Allergen, Product, Order e Invoice