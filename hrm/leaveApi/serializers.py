from rest_framework import serializers
from userApi.models import User
from leaveApi.models import Leave

class LeaveSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        
        model=Leave
        # fields=['id','user','status','date_from','date_to]
        fields = '__all__'