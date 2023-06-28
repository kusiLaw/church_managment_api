from church.models import User, Event
from .serializers import  EventSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class EventsList(APIView):
  '''
    view all events
  '''
  def get(self, request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True, context={'request': request})
    return Response(serializer.data)
  
  def post(self, request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors,)
    

class UserList(APIView):
  def get(self, request):
    users = User.objects.all()
    serializer = UserSerializer(users, many= True, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)