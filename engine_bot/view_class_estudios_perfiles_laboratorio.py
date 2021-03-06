from django.shortcuts import render
from administradores_mhl.Estudios_laboratorio.estudio_laboratorio import *

def estudios_perfiles_laboratorio(request):
    context = {
        #Obtain the first register of the table
        'estudios_perfiles': Estudio.objects.filter(Catalogo = 1).order_by('Nombre')
   
    }
    

    return render(request, 'Small-apps/privacy-policy.html', context)


def estudios_perfiles_laboratorio_id(request, pk):
    context = {
        'estudios_perfiles': Estudio.objects.filter(Clave=pk),
        'condiciones'  : Condiciones.objects.filter(Clave=pk),
    }

    return render(request, 'Small-apps/estudio_perfil_detalle.html', context)


#How to use Truncate on Oracle
#SELECT * FROM (SELECT * FROM TABLE WHERE ROWNUM <= 10) WH