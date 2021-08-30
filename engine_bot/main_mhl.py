from django.shortcuts import render
from estudio_perfil.models import Estudio_perfil


def index(request):
    return render(request, 'Small-apps/index.html')

def contact(request):
    return render(request, 'Small-apps/contact.html')

def sign_in(request):
    return render(request, 'Small-apps/sign-in.html')


def estudios_perfiles_laboratorio(request):
    context = {
        'estudios_perfiles': Estudio_perfil.objects.all()
    }

    return render(request, 'Small-apps/privacy-policy.html', context)