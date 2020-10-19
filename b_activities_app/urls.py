from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register('curso', CursoViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)