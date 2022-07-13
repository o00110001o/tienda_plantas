from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .serializers import *
from app.models import *

    
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all() #va a mostrar todos los productos
    serializer_class = ProductoSerializer #muestra la clase serializadora(serializer)
