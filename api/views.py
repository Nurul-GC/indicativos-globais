from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from api.serializers import UserSerializer, GroupSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class IndicativosViewSet(viewsets.ModelViewSet):
    queryset = ''
    serializer_class = ''
    permission_classes = ['']
