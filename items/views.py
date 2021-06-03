from rest_framework import generics, status, viewsets

from .models import ListContainer, ListItem
from .serializers import ListContainerSerializer, ListItemSerializer


class ListContainerViewSet(viewsets.ModelViewSet):
    queryset = ListContainer.objects.all()
    serializer_class = ListContainerSerializer


class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer
