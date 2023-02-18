from django.contrib.auth.models import User, Group
from .models import Statues
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class StatuesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Statues
        fields = ['name', 'date_construct', 'description', 'size', 'country', 'city', 'img', 'rank', 'cost']