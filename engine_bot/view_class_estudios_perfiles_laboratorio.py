from django.shortcuts import render
from estudio_perfil.models import *

def estudios_perfiles_laboratorio(request):
    context = {
        #Obtain the first register of the table
        'estudios_perfiles': Estudio_perfil.objects.filter(Catalogo = "1")
    }
    print(len(Estudio_perfil.objects.filter(Catalogo = "1")))

    return render(request, 'Small-apps/privacy-policy.html', context)


def estudios_perfiles_laboratorio_id(request, pk):
    context = {
        'estudios_perfiles': Estudio_perfil.objects.filter(Clave=pk),
        'condiciones'  : Condiciones.objects.filter(Clave=pk),
    }

    return render(request, 'Small-apps/estudio_perfil_detalle.html', context)