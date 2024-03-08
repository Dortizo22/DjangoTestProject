from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Correo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tienda'
        verbose_name_plural = 'Tiendas'
        db_table = 'Strore'
        ordering = ['id']

class EmployeeType(models.Model):
    name = models.CharField(max_length=150)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo_de_Usuario'
        verbose_name_plural = 'Tipo_de_Usuarios'
        db_table = 'UserType'
        ordering = ['id']

class Employee(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    email = models.EmailField(max_length=150, verbose_name='Correo electronico', unique=True)
    password = models.CharField(max_length=150, verbose_name='Contrasea')
    date_created = models.DateTimeField(default=datetime.now, verbose_name='Fecha de creación')
    employee = models.ForeignKey(EmployeeType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'User'
        ordering = ['id']


class ProductType(models.Model):
    name = models.CharField(max_length=150, unique=True)
    store = models.ForeignKey(Store, models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo_de_Producto'
        verbose_name_plural = 'Tipo_de_Productos'
        db_table = 'ProductType'
        ordering = ['id']

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    price = models.DecimalField(max_digits=9, default=0.00, decimal_places=2, verbose_name='Precio')
    quantity = models.IntegerField(default=10, verbose_name='Cantidad', max_length=1000)
    product_type = models.ForeignKey(ProductType, models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Product'
        ordering = ['id']


class Customer(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombres')
    email = models.EmailField(max_length=150, verbose_name='Correo electronico')
    dni = models.CharField(max_length=10, verbose_name='Cedula')
    phone = models.CharField(max_length=10, verbose_name='Telefono')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Customer'
        ordering = ['id']

class Sale(models.Model):
    date = models.DateTimeField(default=datetime.now, verbose_name='Fecha de venta')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    iva = models.DecimalField(max_digits=9, decimal_places=2, default=12.00)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'Sale'
        ordering = ['id']

class SaleDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, verbose_name='Cantidad', validators=[MinValueValidator(1), MaxValueValidator(100)])
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Detalle_de_Venta'
        verbose_name_plural = 'Detalle_de_Ventas'
        db_table = 'SaleDetail'
        ordering = ['id']

