from django.shortcuts import render
from administradores_mhl.Estudios_laboratorio.estudio_laboratorio import *


def index(request):
    return render(request, 'Small-apps/index.html')

def contact(request):
    return render(request, 'Small-apps/contact.html')

def sign_in(request):
    return render(request, 'Small-apps/sign-in.html')


