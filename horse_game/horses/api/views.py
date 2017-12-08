from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrAdminOrReadOnly

from .serializers import HorseSerializer
from horses.models import Horse

class HorseViewSet(viewsets.ModelViewSet):
    queryset = Horse.objects.all()
    serializer_class = HorseSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly,)
