#SE ENCARGA DE HACER EL CRUD DESDE JSON

from app.models import *
from rest_framework import serializers
from rest_framework import serializers


class TipoProductoSerializer(serializers.ModelSerializer): #el serializador hace el crud
    class Meta:
        model = TipoProducto
        fields = '__all__' #sirve para cargar todos los campos que tiene el modelo. NO SE USA EN REGISTRO DE USER


class ProductoSerializer(serializers.ModelSerializer):
    
    #DEJA DE MOSTRAR EL TIPO DE PRODUCTO COMO NUMERO Y MUESTRA A QUE CATEGORIA CORRESPONDE  
    tipo = TipoProductoSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = '__all__' #sirve para cargar todos los campos que tiene el modelo. NO SE USA EN REGISTRO DE USER
