from rest_framework import serializers
from feedbackApi.models import Feedback
from userApi.models import User
from leaveApi.models import Leave

class FeedbackSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        
        model=Feedback
        # fields=['id','content','user']
        fields = '__all__'