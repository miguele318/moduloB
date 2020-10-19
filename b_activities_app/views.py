from django.shortcuts import render
from rest_framework import viewsets

from .models import curso
from .serializers import CursoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = curso.objects.all()
    serializer_class = CursoSerializer