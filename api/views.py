from rest_framework import viewsets

from api.models import Indicativos, Paises
from api.serializers import IndicativoSerializer, PaiseSerializer


# Create your views here.
class PaisesViewSet(viewsets.ModelViewSet):
    queryset = Paises.objects.all().order_by('pais')
    serializer_class = PaiseSerializer


class IndicativosViewSet(viewsets.ModelViewSet):
    queryset = Indicativos.objects.all()
    serializer_class = IndicativoSerializer
