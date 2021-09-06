from rest_framework import routers
from .views_drf import *


router = routers.DefaultRouter()

router.register('Estudios y Perfiles de Laboratorio', Estudio_Perfil_Viewset)
