from rest_framework import serializers
from administradores_mhl.Estudios_laboratorio.estudio_laboratorio import *


class Estudio_Perfil_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estudio
        fields = "__all__"
