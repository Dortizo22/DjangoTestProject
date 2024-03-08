from django.db import models
from datetime import datetime

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    email = models.EmailField(max_length=150, verbose_name='Correo electronico', unique=True)
    password = models.CharField(max_length=150, verbose_name='Contrasea')
    date_created = models.DateTimeField(default=datetime.now, verbose_name='Fecha de creación')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'User'
        ordering = ['id']
