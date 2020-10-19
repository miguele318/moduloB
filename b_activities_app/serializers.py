from rest_framework import serializers

from .models import ponenciaCongreso
from .models import publicacion
from .models import curso
from .models import estanciaInvestigacion
from .models import exposicionResultados
from .models import parcipacionProyecto
from .models import premio

from .models import control_matricula

class PonenciaCongresoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ponenciaCongreso
        fields = '__all__'
    
class PublicacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = publicacion
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = curso
        fields = '__all__'

class EstanciaInvestigacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = estanciaInvestigacion
        fields = '__all__'

class ExposicionResultadosSerializer(serializers.ModelSerializer):

    class Meta:
        model = exposicionResultados
        fields = '__all__'

class ParcipacionProyectoSerializer(serializers.ModelSerializer):

    class Meta:
        model = parcipacionProyecto
        fields = '__all__'

class PremioSerializer(serializers.ModelSerializer):

    class Meta:
        model = premio
        fields = '__all__'

# --- #

class control_matriculaSerializer(serializers.ModelSerializer):

    class Meta:
        model = control_matricula
        exclude = [
            'id_matricula','identificacion',
        ]
    