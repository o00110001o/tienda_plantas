import requests #NOS PERMITE LEER EL API
from django.shortcuts import render, redirect
from django.forms import *
from django.contrib import messages
from django.contrib.staticfiles import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate

from app.forms import ProductoForm, CustomUserForm
from app.models import Producto

from .models import *
from .forms import *

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')
    
def base(request):
    return render(request,'base.html')

def ingresar(request):
    return render(request, 'registration/login.html')

def registro(request):
    data = {
        'form': CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar al ususario y redirigirlo al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')

    return render(request, 'registration/registration.html', data)

@login_required
def productos(request):
    #response = requests.get('https://rickandmortyapi.com/productos').json()
    productosAll = Producto.objects.all()
    datos = {'listaProductos' : productosAll }
        #'listaJson': response
       
    if request.method == 'POST':
        carrito = Items_Carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()
        
    return render(request, 'productos.html')

def carrito(request):
    return render(request, 'carrito.html')
    
def test(request):
    data= {
        'form':ProductoForm()
    }

    return render(request, 'test.html', data)

def historial(request):
    return render(request, 'historial.html')

#SECCION LISTAR
@permission_required
def listar_productos(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    
    return render(request, 'templates/productos/listar_productos.html', datos)

#SECCION AGREGAR
@permission_required
def agregar_producto(request):
    data = {
        'form' : ProductoForm()
    } 
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'app/agregar_producto.html'
            

    return render(request, 'agregar_producto.html',data)

#SECCION MODIFICAR
@permission_required
def modificar_producto(request, id):
    producto = Producto.objects.get(id=id)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto modificado correctamente!'
            datos['form'] = formulario

    return render(request, 'app/productos/modificar_producto.html', datos)

# SECCION ELIMINAR
@permission_required
def eliminar_producto (request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return render(to = 'listar_productos.html')