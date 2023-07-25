from church.models import User, Event
from .serializers import  EventSerializer, UserSerializer
from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from django.shortcuts import redirect

@api_view(['GET'])
def default_api_root(request):
    return  redirect('api/v1/')

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