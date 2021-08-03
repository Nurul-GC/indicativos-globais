from api.models import Indicativos, Paises
from rest_framework.serializers import HyperlinkedModelSerializer


class IndicativoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Indicativos
        fields = ['indicativo']


class PaiseSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Paises
        fields = ['pais']
