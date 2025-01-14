from django.shortcuts import render

from rest_framework import viewsets
from .models import UserProfile, Goal
from .serializers import UserProfileSerializer, GoalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .ai_service import generate_mentorship_response

class AIGenerateResponse(APIView):
    def post(self, request):
        user_input = request.data.get('message', '')
        if not user_input:
            return Response({'error': 'No input provided.'}, status=status.HTTP_400_BAD_REQUEST)

        ai_response = generate_mentorship_response(user_input)
        return Response({'response': ai_response}, status=status.HTTP_200_OK)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class AIGenerateResponse(APIView):
    def post(self, request):
        user_input = request.data.get('message', '')
        if not user_input:
            return Response({'error': 'No input provided.'}, status=status.HTTP_400_BAD_REQUEST)

        ai_response = generate_mentorship_response(user_input)
        return Response({'response': ai_response}, status=status.HTTP_200_OK)

