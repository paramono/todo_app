from rest_framework import serializers
from .models import ListContainer, ListItem


class ListContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListContainer
        fields = ['name']


class ListItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListItem
        fields = ['parent', 'name']
