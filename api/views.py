from django.db import router
from rest_framework import viewsets

from api.models import Indicativos
from api.serializers import IndicativoSerializer


# Create your views here.
class IndicativosViewSet(viewsets.ModelViewSet):
    queryset = Indicativos.objects.all()
    serializer_class = IndicativoSerializer
