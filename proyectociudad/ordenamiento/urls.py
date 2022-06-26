"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('barrios', views.listaBarrios,
            name='listaBarrios'),
        path('crear/parroquia', views.crearParroquia,
            name='crearParroquia'),
        path('crear/barrio/<int:id>', views.crearBarrioDeParroquia,
            name='crearBarrioDeParroquia'),
        path('editar/parroquia/<int:id>', views.editarParroquia,
            name='editarParroquia'),
        path('editar/barrio/<int:id>', views.editarBarrio,
            name='editarBarrio'),

 ]