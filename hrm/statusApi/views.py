import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from leaveApi.models import Leave
from leaveApi.models import Leave
from leaveApi.serializers import LeaveSerializer
from userApi.models import User 
from leaveApi.models import Leave

from rest_framework import authentication,permissions



class StatusUpdateView(APIView):
    # permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        user_obj=User.objects.get(id=id)
        leave_obj=Leave.objects.get(user=user_obj)

        serializer=LeaveSerializer(leave_obj)
        return Response(serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        user_obj=User.objects.get(id=id)
        leave_obj=Leave.objects.get(user=user_obj)
        serializer=LeaveSerializer(instance=leave_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
   