from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from app.models import MyUser  
from . serializers import UserSerializer

# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
