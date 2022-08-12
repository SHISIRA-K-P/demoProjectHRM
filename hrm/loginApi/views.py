from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from userApi.serializers import *
from userApi.models import User
from django.contrib.auth import authenticate,login
from rest_framework import authentication,permissions

class SignInView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=LoginSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            uname=serializer.validated_data.get("username")
            password=serializer.validated_data.get("password")
            user=authenticate(request,username=uname,password=password)
            print(user)
            if user:
                login(request,user)
                return Response({"msg":"success"})
            else:
                return Response({"msg":"Invalid credetials"})