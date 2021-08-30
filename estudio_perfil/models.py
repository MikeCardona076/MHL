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
    ('Amarillo', 'Amarillo'),
    ('Dorado', 'Dorado'),
    ('Azul', 'Azul'),
    ('Verde', 'Verde'),
    ('Rojo', 'Rojo'),
    ('Morado', 'Morado'),
    ('Caja de Petri', 'Caja de Petri'),
    ('Culturete', 'Culturete'),
    ('Frasco con Formol', 'Frasco con Formol'),
    ('Frasco esteril', 'Frasco esteril'),
    ('Frasco con aditivo', 'Frasco con aditivo'),
    ('Frasco con medio de Michel', 'Frasco con medio de Michel'),
    ('Exudado', 'Exudado'),
    ('Hisopo', 'Hisopo'),
    ('Frasco PCR', 'Frasco PCR'),
    ('Transporte', 'Transporte'),
    ('Laminilla', 'Laminilla'),
    ('Jeringa', 'Jeringa'),
    ('Trampa', 'Trampa'),
    ('Frotis', 'Frotis'),
    ('Medio para hemocultivo', 'Medio para hemocultivo'),
    ('Contenedor de heces fecales', 'Contenedor de heces fecales'),
)
SEXO_CHOICES = (
    ('Hombre', 'Hombre'),
    ('Mujer', 'Mujer'),
    ('Ambos', 'Ambos'),
)


class Estudio_perfil(models.Model):
    id = models.AutoField(primary_key=True)
    clave = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    subrogado = models.BooleanField(default=False)
    grupo = models.CharField(max_length=100, choices=GROUP_CHOICES)
    contenedor = models.CharField(max_length=100, choices=CONTENT_CHOICES)
    #precio = models.DecimalField(max_digits=10, decimal_places=2)
    #sinonimo1 = models.CharField(max_length=100)
    #sinonimo2 = models.CharField(max_length=100)
    metodo = models.CharField(max_length=100)
    tipo_muestra = models.CharField(max_length=100) 
    equipo = models.CharField(max_length=100)
    indicaciones = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES, default='Ambos')

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        verbose_name_plural = "Estudios Y perfiles"

