from collections import UserList
from re import search
from django.contrib import admin
from.models import *

# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','stock','descripcion','tipo', 'imagen','created_at','updated_at']
    search_fields = ['codigo']
    readonly_fields = ['created_at', 'updated_at']
    list_per_pages = [5]

class UserAdmin(admin.ModelAdmin):
    list_display = ['run','nombre','apellido','email',' contraseña','sub']
    search_fields = ['run']
    list_per_page = [5]

class Usuario(admin.ModelAdmin):
    list_display = ['nombre','apellido','correo','password','created_at','updated_at']
    search_fields = ['nombre']
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = []

admin.site.register(Producto, ProductosAdmin)
#admin.site.register(Usuario,UserAdmin)
admin.site.register(TipoProducto)
#admin.site.register(Usuario, UserList)