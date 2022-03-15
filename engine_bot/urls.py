from django.urls import path
from .main_mhl import *
from .view_class_estudios_perfiles_laboratorio import *



ESTUDIOS_PERFILES_URL = [
    path('estudios_perfiles_laboratorio/', estudios_perfiles_laboratorio, name='estudios_perfiles_laboratorio'),
    path('Detalle/<int:pk>/', estudios_perfiles_laboratorio_id, name='Detalle_estudio'),
]

# PACIENTES_PXLABS_URL = [
#     path('pacientes_pxlab/', pacientes_pxlab, name='pacientes_pxlab'),
# ]


urlpatterns = [
    path('', index, name='index'),
    path('contac/', contact, name='contact'),
    path('sign_in/', sign_in, name='sign_in'),
]  + ESTUDIOS_PERFILES_URL 
