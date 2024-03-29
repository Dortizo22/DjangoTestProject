# Generated by Django 5.0.3 on 2024-03-08 15:28

import datetime
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombres')),
                ('email', models.EmailField(max_length=150, verbose_name='Correo electronico')),
                ('dni', models.CharField(max_length=10, verbose_name='Cedula')),
                ('phone', models.CharField(max_length=10, verbose_name='Telefono')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'Customer',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EmployeeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tipo_de_Usuario',
                'verbose_name_plural': 'Tipo_de_Usuarios',
                'db_table': 'UserType',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo_de_Producto',
                'verbose_name_plural': 'Tipo_de_Productos',
                'db_table': 'ProductType',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Correo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Tienda',
                'verbose_name_plural': 'Tiendas',
                'db_table': 'Strore',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='Correo electronico')),
                ('password', models.CharField(max_length=150, verbose_name='Contrasea')),
                ('date_created', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de creación')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.employeetype')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'User',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio')),
                ('quantity', models.IntegerField(default=10, max_length=1000, verbose_name='Cantidad')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.producttype')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Product',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de venta')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('iva', models.DecimalField(decimal_places=2, default=12.0, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.employee')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'db_table': 'Sale',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Cantidad')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.sale')),
            ],
            options={
                'verbose_name': 'Detalle_de_Venta',
                'verbose_name_plural': 'Detalle_de_Ventas',
                'db_table': 'SaleDetail',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='producttype',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.store'),
        ),
        migrations.AddField(
            model_name='employeetype',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.store'),
        ),
    ]
