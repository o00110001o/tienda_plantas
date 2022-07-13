#CORRESPONDE A LAS URLS QUE SE UTILIZARAN   
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter() #Nos entrega el enrutador por defecto/ ahora se puede modificar
router.register('producto', ProductoViewSet) # esta con la de arriba generan el get y el post

app_name = 'apiapp'
urlpatterns = [
    path('api/', include(router.urls)), # estamos levantando el admin
    
]
