from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_jwt.utils import jwt_encode_handler
from django.contrib.auth.models import User
from utils import generate_jwt_token

# Create your views here.

@authentication_classes(['rest_framework_jwt.authentication.JSONWebTokenAuthentication'])
@permission_classes([IsAuthenticated])
class SecureView(APIView):
    def get(self, request):
        return Response({'message': 'You are authenticated!'})

class CustomAuthView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user_id = 1
        payload = {'user_id': user_id}
        token = jwt_encode_handler(payload)
        return Response({'token': token})

class UserRegistrationView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        new_user = User.objects.create_user(username=username, password=password)
        user_id = new_user.id
        payload = {'user_id': user_id}
        token = jwt_encode_handler(payload)
        return Response({'token': token})

class CustomView(APIView):
    def post(self, request):
        token = generate_jwt_token(1)
        return Response({'token': token})