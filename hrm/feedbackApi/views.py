import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feedback
from feedbackApi.serializers import FeedbackSerializer
from userApi.models import User 
from django.contrib.auth import authenticate,login
from rest_framework import authentication,permissions


class FeedbackView(APIView):
    # permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        feedback_obj=Feedback.objects.all()
        serializer=FeedbackSerializer(feedback_obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        serializer=FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class FeedbackDetailView(APIView):
    # permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        feedback_obj=Feedback.objects.get(id=id)
        serializer=FeedbackSerializer(feedback_obj)
        return Response(serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        feedback_obj=Feedback.objects.get(id=id)
        serializer=FeedbackSerializer(instance=feedback_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        feedback_obj=Feedback.objects.get(id=id)
        feedback_obj.delete()
        return Response({"msg":"deleted"})
