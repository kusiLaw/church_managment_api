from church.models import User, Event
from .serializers import  EventSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets, permissions
from .permissions import IsOwnerOrReadOnly
class  EventViewSet(viewsets.ModelViewSet):
  """
    Only add has permission to full control 
    All users can only read events
  """
  queryset = Event.objects.all()
  serializer_class = EventSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.

    viewsets combines list and details into a single viewset
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]