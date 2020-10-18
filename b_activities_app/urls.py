from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from b_activities_app.views import *

urlpatterns = []
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)