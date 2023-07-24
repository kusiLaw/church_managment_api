from church.models import User, Event
from .serializers import  EventSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets, permissions
from .permissions import IsOwnerOrReadOnly
class  EventViewSet(viewsets.ReadOnlyModelViewSet):
  """ 
    All users can only read events
  """
  queryset = Event.objects.all()
  serializer_class = EventSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.

    viewsets combines list and details into a single viewset
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]