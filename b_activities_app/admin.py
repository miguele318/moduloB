from django.contrib import admin
from .models import *

'''
class ponenciaCongresoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class publicacionAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class cursoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class exposicionResultadosAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class estanciaInvestigacionAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class parcipacionProyectoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
'''

admin.site.register([
    ponenciaCongreso,
    publicacion,
    curso,
    exposicionResultados,
    estanciaInvestigacion,
    parcipacionProyecto,
    premio
])