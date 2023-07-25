from django.urls import path,include
from .views import *

urlpatterns = [
path('inicio/', inicio, name='inicio-lab'), 
path('insertar/', insertar_lab, name='insertar-lab'), 
path('mostrar/', mostrar_lab, name='mostrar-lab'), 
path('editar/<int:pk>', editar_lab, name='editar-lab'), 
path('actualizar/<int:pk>', actualizar_lab, name='actualizar-lab'), 
path('eliminar/<int:pk>', eliminar_lab, name='eliminar-lab'),
]