from rest_framework.serializers import HyperlinkedModelSerializer
from indig.models import Indicativos


class IndicativoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Indicativos
