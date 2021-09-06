from django.db import models

class Estudio_perfil(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50, null=True, blank=True)
    Precio1 = models.CharField(max_length=10,null=True, blank=True)
    Precio2 = models.CharField(max_length=10, null=True, blank=True)
    Precio3 = models.CharField(max_length=10, null=True, blank=True)
    Precio4 = models.CharField(max_length=10, null=True, blank=True)
    Precio5 = models.CharField(max_length=10,  null=True, blank=True)
    Prupo = models.CharField(max_length=50, null=True, blank=True)
    Tipo = models.CharField(max_length=50, null=True, blank=True)
    Sinonimo1 = models.CharField(max_length=50, null=True, blank=True)
    Sinonimo2 = models.CharField(max_length=50, null=True, blank=True)
    Tubo = models.CharField(max_length=50, null=True, blank=True)
    Unidades = models.CharField(max_length=50, null=True, blank=True)
    Metodo = models.CharField(max_length=50, null=True, blank=True)
    TipoMuestra = models.CharField(max_length=50, null=True, blank=True)
    Catalogo = models.CharField(max_length=50, null=True, blank=True)
    Tiempo = models.CharField(max_length=50, null=True, blank=True)
    Costo = models.CharField(max_length=10, null=True, blank=True)
    Especiales = models.CharField(max_length=50, null=True, blank=True)
    SexoPrueba = models.CharField(max_length=50, null=True, blank=True)
    Clasifica = models.CharField(max_length=50, null=True, blank=True)
    EstLaboratorio = models.CharField(max_length=50, null=True, blank=True)
    EstGabinete = models.CharField(max_length=50, null=True, blank=True)
    Factor = models.CharField(max_length=10,  null=True, blank=True)
    UnidadesInt = models.CharField(max_length=50, null=True, blank=True)
    TdContenedor = models.CharField(max_length=50, null=True, blank=True)
    Equipo = models.CharField(max_length=50, null=True, blank=True)
    Maquilador = models.CharField(max_length=50, null=True, blank=True)
    Indicaciones = models.CharField(max_length=50, null=True, blank=True)
    Area = models.CharField(max_length=50, null=True, blank=True)
    usoClinico = models.CharField(max_length=50, null=True, blank=True)
    nivelBase = models.CharField(max_length=50, null=True, blank=True)
    tProceso = models.CharField(max_length=50, null=True, blank=True)
    CodigoSAT = models.CharField(max_length=50, null=True, blank=True)
    UnidadSAT = models.CharField(max_length=50, null=True, blank=True)
    ImpConsent = models.CharField(max_length=50, null=True, blank=True)
    GpoRecep = models.CharField(max_length=50, null=True, blank=True)
    ClaveExt = models.CharField(max_length=50, null=True, blank=True)
    Moneda = models.CharField(max_length=50, null=True, blank=True)
    impSep = models.CharField(max_length=50, null=True, blank=True)
    impNombreP = models.CharField(max_length=50, null=True, blank=True)
    IdTipoMuestra = models.CharField(max_length=50, null=True, blank=True)
    IdGrupo = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        id_Estudio_perfil = '%s' % (self.id)
        return id_Estudio_perfil

        
    class Meta:
        managed = True
        db_table = 'estudio_perfil'
    
#Clave	Nombre	Grupo	Condicion	Descripcion

class Condiciones(models.Model):
    id = models.AutoField(primary_key=True)
    Clave = models.ForeignKey(Estudio_perfil, on_delete=models.CASCADE, null=True, blank=True)
    Nombre = models.CharField(max_length=50, null=True, blank=True)
    Grupo = models.CharField(max_length=50, null=True, blank=True)
    Condicion = models.CharField(max_length=50, null=True, blank=True)
    Descripcion = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'Condiciones'

    if Clave not in Estudio_perfil.objects.all():
        Clave = " "

    def __str__(self):
        id_Condicion = '%s' % (self.id)
        return id_Condicion


    






    
    


 
    
