from rest_framework import serializers, status
from rest_framework.exceptions import ParseError
from church.models import User, Event
from django.utils import timezone
from datetime import datetime


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'first_name', 'last_name', 'email')



class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = '__all__'
 
  # def get_days(self, obj):
  #   # Todo: work on days left
  #   pass
    # return datetime(year=obj.start_date.year , month=obj.start_date.month, day=obj.start_date.day) - datetime.now()

  def validate(self, data):
    if data['start_date'] > data['end_date']:
      raise ParseError(detail="Start date can not be greater than end date", code=400)
    date =  timezone.now()                         
    if datetime(data['end_date'].year, data['end_date'].month,data['end_date'].day ) < datetime(date.year, date.month, date.day, date.hour, date.minute):
      raise ParseError(detail="Sorry, can't process your request. This event is ended already", code=400)
    return data