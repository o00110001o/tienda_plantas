from django.contrib import admin
from django.urls.conf import path
from django.urls import path,include
#from app import admin as appad
from app.views import *
 
urlpatterns = [
    path('', index, name="index"),
    path('home/', home, name="home"),
    path('carrito/', carrito, name="carrito"),
    path('historial/', historial, name="historial"),
    path('productos/', productos,name="productos"),
#----------------------------------------------------------------------
    path('test/', test, name="test"),
    path('base/', base, name="base.html"),
#----------------------------------------------------------------------
    path('accounts/', include('django.contrib.auth.urls')),
    path('ingresar/', ingresar,name="login"),
    path('registro/', registro, name='registration'),
#----------------------------------------------------------------------
    path('historial/', historial, name="historial"),
#----------------------------------------------------------------------
    path('agregar/', agregar_producto, name="agregar_productos"),
    path('modificar/', modificar_producto, name="modificar_productos"),
    path('listar/', listar_productos, name="listar_productos"),
]
