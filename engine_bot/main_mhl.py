from django.shortcuts import render

def index(request):
    return render(request, 'Small-apps/index.html')

def contact(request):
    return render(request, 'Small-apps/contact.html')

def sign_in(request):
    return render(request, 'Small-apps/sign-in.html')

def estudios_perfiles_laboratorio(request):
    return render(request, 'Small-apps/privacy-policy.html')