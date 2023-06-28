from church.models import User, Event
from .serializers import  EventSerializer
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
    

# class EventDetail(APIView):
#   def get(self, request):
#     event = Event.objects.get(id=request.data['id'])
#     serializer = EventSerializer(event, context={'request': request})
#     return Response(serializer.data)