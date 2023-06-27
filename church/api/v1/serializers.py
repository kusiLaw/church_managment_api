from rest_framework import serializers
from church.models import User, Event


class EventSerializer(serializers.ModelSerializer):
  # id = serializers.IntegerField(read_only=True)
  class Meta:
    model = Event
    fields = '__all__'
    # exclude = ['id']