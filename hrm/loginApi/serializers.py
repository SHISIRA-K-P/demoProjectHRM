from rest_framework import serializers
from userApi.models import User

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()