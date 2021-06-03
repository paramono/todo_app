from rest_framework import serializers
from .models import ListContainer, ListItem


class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItem
        fields = ['id', 'parent', 'name', 'done']


class ListContainerSerializer(serializers.ModelSerializer):
    items = ListItemSerializer(many=True, required=False)

    class Meta:
        model = ListContainer
        fields = ['id', 'name', 'items']
