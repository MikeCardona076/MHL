from rest_framework import viewsets
from administradores_mhl.Estudios_laboratorio.estudio_laboratorio import *
from .serializer import *


class Estudio_Perfil_Viewset(viewsets.ModelViewSet):
    queryset = Estudio.objects.all()
    serializer_class = Estudio_Perfil_Serializer