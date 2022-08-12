from rest_framework import serializers
from userApi.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','first_name','last_name','username','email','password','phone']
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()