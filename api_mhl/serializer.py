from rest_framework import serializers
from estudio_perfil.models import *


class Estudio_Perfil_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estudio_perfil
        fields = "__all__"
