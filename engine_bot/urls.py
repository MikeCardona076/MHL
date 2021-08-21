from django.urls import path
from .main_mhl import *
from estudio_perfil.class_views import *




urlpatterns = [
    path('', index, name='index'),
    path('contac/', contact, name='contact'),
    path('sign_in/', sign_in, name='sign_in'),
    path('estudios_perfiles_laboratorio/', estudios_perfiles_laboratorio, name='estudios_perfiles_laboratorio'),

] 
