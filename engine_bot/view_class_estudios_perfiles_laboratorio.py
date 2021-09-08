from django.shortcuts import render
from estudio_perfil.models import *

def estudios_perfiles_laboratorio(request):
    context = {
        #Obtain the first register of the table
        'estudios_perfiles': Estudio_perfil.objects.filter(),
        'Condiciones' : Condiciones.objects.all(),
    }

    return render(request, 'Small-apps/privacy-policy.html', context)