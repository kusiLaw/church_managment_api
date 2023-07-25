from church.models import User, Event
from .serializers import  EventSerializer, UserSerializer
from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnly

class  EventViewSet(viewsets.ReadOnlyModelViewSet):
  """ 
    All users can only read events
  """
  queryset = Event.objects.all()
  serializer_class = EventSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    viewsets combines list and details into a single viewset
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]