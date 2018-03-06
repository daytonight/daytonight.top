from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
# ViewSets define the view behavior.
from rest_framework import viewsets

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer