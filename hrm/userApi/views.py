import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from userApi.serializers import UserSerializer
from userApi.models import User 
from django.contrib.auth import authenticate,login
from rest_framework import authentication,permissions


class UserView(APIView):
    # permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        user_obj=User.objects.all()
        serializer=UserSerializer(user_obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    # permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        user_obj=User.objects.get(id=id)
        serializer=UserSerializer(user_obj)
        return Response(serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        patient_obj=User.objects.get(id=id)
        serializer=UserSerializer(instance=patient_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        user_obj=User.objects.get(id=id)
        user_obj.delete()
        return Response({"msg":"deleted"})
