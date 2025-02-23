from django.urls import path
from .views_web import CompanyListView, CompanyCreateView, CompanyUpdateView, CompanyDeleteView

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/create/', CompanyCreateView.as_view(), name='company-create'),
    path('companies/<int:pk>/update/', CompanyUpdateView.as_view(), name='company-update'),
    path('companies/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company-delete'),

    # Repite para User, Allergen, Product, Order e Invoice
]