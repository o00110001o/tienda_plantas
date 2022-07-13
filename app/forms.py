from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import*
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#template para crear el formulario
class ProductoForm(ModelForm):

    nombre = forms.CharField(min_length=10,max_length=20)
    precio = forms.IntegerField(min_value=400)
	
    widgets = {
      'fecha_ingreso' : forms.SelectDateWidget(years=range(2022,2023))
    }

    class Meta:
        model = Producto
        fields = ['codigo','nombre','marca','precio','stock','descripcion','tipo','imagen','created_at', 'updated_at']
        enctype="multipart/form-data"

class CustomUserForm(UserCreationForm):
  
  class Meta:
    model = User
    fields = ['first_name','last_name','email','username','password1','password2']