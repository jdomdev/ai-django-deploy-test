from rest_framework import viewsets
from .models import Company, User# , Allergen, Product, Order, Invoice
from .serializers import CompanySerializer, UserSerializer# , AllergenSerializer, ProductSerializer, OrderSerializer, InvoiceSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Repite para Allergen, Product, Order e Invoice