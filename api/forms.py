from django import forms
from .models import Company, User, Allergen, Product, Order, Invoice

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

# Repite para Allergen, Product, Order e Invoice