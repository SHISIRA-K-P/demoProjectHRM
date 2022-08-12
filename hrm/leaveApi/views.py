import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Leave
from leaveApi.models import Leave
from leaveApi.serializers import LeaveSerializer
from userApi.models import User 
from django.contrib.auth import authenticate,login
# from rest_framework import authentication,permissions

import logging as log



class LeaveView(APIView):
    # permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        leave_obj=Leave.objects.all()
        log.info("Retrieve  all object")
        serializer=LeaveSerializer(leave_obj,many=True)
        log.info("serializing data")
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        serializer=LeaveSerializer(data=request.data)
        log.info("serializing data")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LeaveDetailView(APIView):
    # permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        leave_obj=Leave.objects.get(id=id)
        log.info("Retrieve  an object with specific id")
        serializer=LeaveSerializer(leave_obj)
        return Response(serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        leave_obj=Leave.objects.get(id=id)
        serializer=LeaveSerializer(instance=leave_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        leave_obj=Leave.objects.get(id=id)
        leave_obj.delete()
        log.info("object deleted")
        return Response({"msg":"deleted"})
