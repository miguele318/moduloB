from django.shortcuts import render
from rest_framework import viewsets

from .models import ponenciaCongreso
from .serializers import PonenciaCongresoSerializer
from .models import publicacion
from .serializers import PublicacionSerializer
from .models import curso
from .serializers import CursoSerializer
from .models import estanciaInvestigacion
from .serializers import EstanciaInvestigacionSerializer
from .models import exposicionResultados
from .serializers import ExposicionResultadosSerializer
from .models import parcipacionProyecto
from .serializers import ParcipacionProyectoSerializer
from .models import premio
from .serializers import PremioSerializer

class PonenciaCongresoViewSet(viewsets.ModelViewSet):
    queryset = ponenciaCongreso.objects.all()
    serializer_class = PonenciaCongresoSerializer

class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = publicacion.objects.all()
    serializer_class = PublicacionSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = curso.objects.all()
    serializer_class = CursoSerializer

class EstanciaInvestigacionViewSet(viewsets.ModelViewSet):
    queryset = estanciaInvestigacion.objects.all()
    serializer_class = EstanciaInvestigacionSerializer

class ExposicionResultadosViewSet(viewsets.ModelViewSet):
    queryset = exposicionResultados.objects.all()
    serializer_class = ExposicionResultadosSerializer

class ParcipacionProyectoViewSet(viewsets.ModelViewSet):
    queryset = parcipacionProyecto.objects.all()
    serializer_class = ParcipacionProyectoSerializer

class PremioViewSet(viewsets.ModelViewSet):
    queryset = premio.objects.all()
    serializer_class = PremioSerializer
