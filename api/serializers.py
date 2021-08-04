from rest_framework.serializers import HyperlinkedModelSerializer

from api.models import Indicativos


class IndicativoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Indicativos
        fields = ['id', 'pais']
