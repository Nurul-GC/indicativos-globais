from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from api.serializers import UserSerializer, GroupSerializer


# Create your views here.
class IndicativosViewSet(viewsets.ModelViewSet):
    queryset = ''
    serializer_class = ''
    permission_classes = ['']
