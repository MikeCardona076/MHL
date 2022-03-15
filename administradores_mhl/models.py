from django.db import models

# Create your models here.


class Administrador_mhl(models.Model):
    nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    cedula = models.CharField(max_length=10, blank=True, null=True)
    titulo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno