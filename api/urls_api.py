from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import CompanyViewSet, UserViewSet#, AllergenViewSet, ProductViewSet, OrderViewSet, InvoiceViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'users', UserViewSet)
""" router.register(r'allergens', AllergenViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'invoices', InvoiceViewSet) """

urlpatterns = [
    path('', include(router.urls)),
]