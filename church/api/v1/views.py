from church.models import User, Event
from .serializers import  EventSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets

# class EventsList(APIView):
#   '''
#     view all events
#   '''
#   def get(self, request):
#     events = Event.objects.all()
#     serializer = EventSerializer(events, many=True, context={'request': request})
#     return Response(serializer.data)
  
#   def post(self, request):
#     serializer = EventSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     else:
#       return Response(serializer.errors,)
    

class  EventViewSet(viewsets.ModelViewSet):
  """
    Only add has permission to full control 
    All users can only read events
  """
  queryset = Event.objects.all()
  serializer_class = EventSerializer



class UserList(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  pass