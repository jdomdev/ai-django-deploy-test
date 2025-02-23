from django.db import models

class Company(models.Model):
    address = models.CharField(max_length=255)
    tax_number = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.email

class User(models.Model):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

class Allergen(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    stock = models.IntegerField()
    image_url = models.URLField()
    net_price = models.DecimalField(max_digits=10, decimal_places=2)
    allergen = models.ForeignKey(Allergen, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    table_number = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    dish_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Order {self.id} by {self.user.name}"

class Invoice(models.Model):
    date = models.DateTimeField()
    payment_method = models.CharField(max_length=50)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice {self.id}"