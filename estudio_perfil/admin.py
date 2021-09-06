from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from django.contrib import admin
from .models import *
from django.contrib.admin.models import LogEntry



# Register your models here.

admin.site.register(LogEntry)


#IMPORT EXPORT ESTUIDOS DE LABORATORIO
class EstudiosResource(resources.ModelResource):
    class Meta:
        model = Estudio_perfil
        fields = ('id', 'Nombre', 'Precio1', 'Precio2', 'Precio3', 'Precio4', 'Precio5', 'Grupo', 'Tipo', 'Sinonimo1', 'Sinonimo2', 'Tubo', 'Unidades', 'Metodo', 'TipoMuestra', 'Catalogo', 'Tiempo', 'Costo', 'Especiales', 'SexoPrueba', 'Clasifica', 'EstLaboratorio', 'EstGabinete', 'Factor', 'UnidadesInt', 'IdContenedor', 'Equipo', 'Maquilador', 'Indicaciones', 'Area', 'usoClinico', 'nivelBase', 'tProceso', 'CodigoSAT', 'UnidadSAT', 'ImpConsent', 'GpoRecep', 'ClaveExt', 'Moneda', 'impSep', 'impNombreP', 'IdTipoMuestra', 'IdGrupo')


class EstudiosAdmin(ImportExportModelAdmin):
    resource_class = EstudiosResource
 


admin.site.register(Estudio_perfil, EstudiosAdmin)



#IMPORT EXPORT ESTUIDOS DE Condiciones
class CondicionesResource(resources.ModelResource):
    class Meta:
        model = Condiciones
        fields = ('id', 'Clave', 'Nombre', 'Grupo', 'Condicion', 'Descripcion')


class CondicionesAdmin(ImportExportModelAdmin):
    resource_class = CondicionesResource
    


admin.site.register(Condiciones, CondicionesAdmin)
