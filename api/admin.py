from django.contrib import admin
from .models import Company, User, Allergen, Product, Order, Invoice

# Registrar los modelos en el admin
admin.site.register(Company)
admin.site.register(User)
admin.site.register(Allergen)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Invoice)