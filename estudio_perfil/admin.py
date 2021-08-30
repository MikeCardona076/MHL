from django.contrib import admin
from .models import Estudio_perfil
from django.contrib.admin.models import LogEntry



# Register your models here.



admin.site.register(LogEntry)
admin.site.register(Estudio_perfil)






