from django.urls import path
from .main_mhl import *
from .view_class_estudios_perfiles_laboratorio import *
from  chat_bot.views import  ChatterBotAppView, ChatterBotApiView


ESTUDIOS_PERFILES_URL = [
    path('estudios_perfiles_laboratorio/', estudios_perfiles_laboratorio, name='estudios_perfiles_laboratorio'),
    path('Detalle/<int:pk>/', estudios_perfiles_laboratorio_id, name='Detalle_estudio'),
    path('estudios_perfiles_laboratorio/<int:pk>/', estudios_perfiles_laboratorio_id, name='estudios_perfiles_laboratorio_id'),
    path('api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
    path('main/', ChatterBotAppView.as_view(), name='main'),
]

# PACIENTES_PXLABS_URL = [
#     path('pacientes_pxlab/', pacientes_pxlab, name='pacientes_pxlab'),
# ]


urlpatterns = [
    path('', index, name='index'),
    path('contac/', contact, name='contact'),
    path('sign_in/', sign_in, name='sign_in'),
]  + ESTUDIOS_PERFILES_URL 
