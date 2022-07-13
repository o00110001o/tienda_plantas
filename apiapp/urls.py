#CORRESPONDE A LAS URLS QUE SE UTILIZARAN   
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)

app_name = 'apiapp'
urlpatterns = [
    path('api/', include(router.urls)), # estamos levantando el admin
    
]
