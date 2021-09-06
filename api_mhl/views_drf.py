from rest_framework import viewsets
from estudio_perfil.models import *
from .serializer import *


class Estudio_Perfil_Viewset(viewsets.ModelViewSet):
    queryset = Estudio_perfil.objects.all()
    serializer_class = Estudio_Perfil_Serializer