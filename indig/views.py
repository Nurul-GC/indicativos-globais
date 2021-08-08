from rest_framework import viewsets
from indig.models import Indicativos
from indig.serializers import IndicativoSerializer


# Create your views here.
class IndicativosViewSet(viewsets.ModelViewSet):
    serializer_class = IndicativoSerializer
