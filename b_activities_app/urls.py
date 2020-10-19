from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('ponenciaCongreso', PonenciaCongresoViewSet)
router.register('publicacion', PublicacionViewSet)
router.register('curso', CursoViewSet)
router.register('estanciaInvestigacion', EstanciaInvestigacionViewSet)
router.register('exposicionResultados', ExposicionResultadosViewSet)
router.register('parcipacionProyecto', ParcipacionProyectoViewSet)
router.register('premio', PremioViewSet)

router.register(r'periodo', control_matriculaViewSet, basename='control_matricula')

urlpatterns = [
    path('api/', include(router.urls))
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)