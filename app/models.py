from datetime import datetime
from statistics import mode
from unittest.mock import create_autospec
from django.db import models


# Create your models here.

class TipoProducto(models.Model):
    tipo = models.CharField(max_length=75)
    def __str__(self):
        return self.tipo

class Producto(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    created_at =  models.DateField(auto_now_add=False,default=datetime.utcnow)
    updated_at =  models.DateField(auto_now=False, default=datetime.utcnow)

    def __str__(self):
        return str(self.tipo)

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField (max_length=20)
    correo = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    created_at =  models.DateField(auto_now_add=False)
    updated_at =  models.DateField(auto_now=False)
    
    def __str__(self):
        return self.tipo

class TipoUsuario(models.Model):
    tipo = models.CharField(max_length=75)
    def __str__(self):
        return self.tipo

class Items_Carrito(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="items_carrito", null=True)

    def __str__(self):
        return self.nombre
        
    class Meta:
        db_table = 'db_items_carrito'



