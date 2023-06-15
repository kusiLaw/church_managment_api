from church.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def users(request):
  users = User.objects.all()
  users =  UserSerializer(users, many=True).data
  return Response(users)


@api_view()
def user_detail(request, pk):
  try:
    user = User.objects.get(pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)
  except User.DoesNotExist:
    return Response(status='not found')