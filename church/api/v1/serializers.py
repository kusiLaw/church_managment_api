from rest_framework import serializers
from church.models import User

class UserSerializer(serializers.ModelSerializer):
  id = serializers.IntegerField(read_only=True)
  first_name = serializers.CharField()
  last_name = serializers.EmailField()
  email = serializers.EmailField()

  class Meta:
    model = User
    fields = ('id', 'first_name', 'last_name', 'email')