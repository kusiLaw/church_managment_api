from django.shortcuts import render
from .models import User, Membership
from django.http import JsonResponse


# Create your views here.
def index(request):
  obj = User.objects.all()
  memb = Membership.objects.all()
  data = {
    'data': list(obj.values()),
    'membership': list(memb.values())
          }
  return JsonResponse(data)


def user_detail(request, id):
  obj = User.objects.get(pk=id)
  data = {
    'data': [{
      'name': obj.first_name,
      'last_name': obj.last_name,

    }]
          }
  return JsonResponse(data)