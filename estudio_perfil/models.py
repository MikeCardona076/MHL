from django.db import models


GROUP_CHOICES = (
    #Biologia molecular
    ('Biologia molecular', 'Biologia molecular'),
    #Inmunoligia
    ('Inmunoligia', 'Inmunoligia'),
    #Uroanalisi y Coprologia
    ('Uroanalisi y Coprologia', 'Uroanalisi y Coprologia'),
    #Hematologia y coagulacion
    ('Hematologia y coagulacion', 'Hematologia y coagulacion'),
    #Microbiologia
    ('Microbiologia', 'Microbiologia'),
    #Anatomia y Patologia 
    ('Anatomia y Patologia', 'Anatomia y Patologia'),
    #Hemostasia
    ('Hemostasia', 'Hemostasia'),
)


CONTENT_CHOICES = (
    ('Amarillo', '01'),
    ('Dorado', '04'),
    ('Azul', '03'),
    ('Verde', '05'),
    ('Rojo', '06'),
    ('Morado', '02'),
    ('Caja de Petri', '07'),
    ('Culturete', '08'),
    ('Frasco con Formol', '09'),
    ('Frasco esteril', '010'),
    ('Frasco con aditivo', '011'),
    ('Frasco con medio de Michel', '012'),
    ('Exudado', '013'),
    ('Hisopo', '014'),
    ('Frasco PCR', '015'),
    ('Transporte', '016'),
    ('Laminilla', '017'),
    ('Jeringa', '018'),
    ('Trampa', '019'),
    ('Frotis', '020'),
    ('Medio para hemocultivo', '021'),
    ('Contenedor de heces fecales', '022'),
)


class Estudio_perfil(models.Model):
    id = models.AutoField(primary_key=True)
    clave = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    subrogado = models.BooleanField(default=False)
    grupo = models.CharField(max_length=100, choices=GROUP_CHOICES)
    contenedor = models.CharField(max_length=100, choices=CONTENT_CHOICES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    sinonimo1 = models.CharField(max_length=100)
    sinonimo2 = models.CharField(max_length=100)
    metodo = models.CharField(max_length=100)
    tipo_muestra = models.CharField(max_length=100)
    equipo = models.CharField(max_length=100)
    indicaciones = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        verbose_name_plural = "Estudios Y perfiles"

