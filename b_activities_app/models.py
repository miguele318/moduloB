from django.db import models
from django.contrib.auth.models import User        # TODO: Actualizar usuario a estudiante

class actividad(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    #id_evaluacion_coo = models.PositiveIntegerField() #
    #id_evaluacion_dir = models.PositiveIntegerField() #
    identificacion = models.PositiveIntegerField() # models.ForeignKey(User, on_delete=models.CASCADE) #TODO: Relacionar a usuario
    titulo = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=False, null=False)
    justificante = models.FileField(upload_to="b_activities_app/archivos", blank=False, null=False)
    estado = models.CharField(max_length=20, blank=False, null=False)
    fecha_inicio = models.DateField(blank=False, null=False)
    fecha_fin = models.DateField(blank=True, null=True)
    anio_academico = models.CharField(max_length=20, blank=False, null=False)
    tipo = models.CharField(max_length=50, blank=False, null=False)

class ponenciaCongreso(actividad):
    id_ins = models.PositiveIntegerField() #TODO: Relacionar con institucion (EntidadOrganizadora)
    lugar = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name='Ponencia en congreso / Simposio / Jornada'
        verbose_name_plural='Ponencias en congresos / Simposios / Jornadas'
    
    def __str__(self):
        return self.nombre

class publicacion(actividad):
    tipo_pub = models.CharField(max_length=100, blank=False, null=False)
    autores = models.CharField(max_length=255, blank=False, null=False)
    datos_generales = models.CharField(max_length=255, blank=False, null=False)
    editorial = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name='Publicación'
        verbose_name_plural='Publicaciones'
    
    def __str__(self):
        return self.nombre

class curso(actividad):
    id_programa = models.PositiveIntegerField() #TODO: Relacionar con programa
    horas_asignadas = models.PositiveIntegerField(blank=False, null=False)

    class Meta:
        verbose_name='Curso / Direccion de proyectos / Revision de proyectos'
        verbose_name_plural='Cursos / Direcciones de proyectos / Revisiones de proyectos'
    
    def __str__(self):
        return self.nombre

class estanciaInvestigacion(actividad):
    id_ins = models.PositiveIntegerField() #TODO: Relacionar con institucion (De aqui se saca la relacion con ciudad y pais)
    proposito = models.CharField(max_length=25, blank=False, null=False)
    responsable = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name='Estancia de investigación en otras instituciones'
        verbose_name_plural='Estancias de investigación en otras instituciones'
    
    def __str__(self):
        return self.nombre

class exposicionResultados(actividad):
    modalidad = models.CharField(max_length=100, blank=False, null=False)
    duracion = models.CharField(max_length=20, blank=False, null=False)
    lugar = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name='Exposición de resultados parciales de investigación'
        verbose_name_plural='Exposiciónes de resultados parciales de investigación'
    
    def __str__(self):
        return self.nombre

class parcipacionProyecto(actividad):
    id_linea_invs = models.PositiveIntegerField() #TODO: Relacionar a linea_Investifacion
    id_investigador = models.PositiveIntegerField() #TODO: Relacionar a profesor
    lugar = models.CharField(max_length=50, blank=False, null=False)
    codigoVRI = models.IntegerField(blank=False, null=False)
    convocatoria = models.CharField(max_length=50, blank=False, null=False)
    tipo_convocatoria = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name='Participación en proyecto de investigación'
        verbose_name_plural='Participaciónes en proyectos de investigación'
    
    def __str__(self):
        return self.nombre

class premio(models.Model):
    id_premio = models.AutoField(primary_key=True)
    id_actividad = models.ForeignKey(actividad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20, blank=False, null=False)

    class Meta:
        verbose_name='Premio'
        verbose_name_plural='Premios'

    def __str__(self):
        return self.nombre