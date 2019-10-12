from rest_framework import viewsets
from rest_framework.response import Response
from accounts.models import Profile
from .serializers import *
from rest_framework.authentication  import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics

class ProfileViewList(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileViewDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
