from django.shortcuts import render

from rest_framework import viewsets
from .models import UserProfile, Goal
from .serializers import UserProfileSerializer, GoalSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

