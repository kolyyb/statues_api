from django.contrib.auth.models import User, Group
from .models import Statues
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer, StatuesSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class StatuesViewSet(viewsets.ModelViewSet):
    queryset = Statues.objects.all().order_by('-rank')
    serializer_class = StatuesSerializer
    permission_classes = [permissions.IsAuthenticated]




