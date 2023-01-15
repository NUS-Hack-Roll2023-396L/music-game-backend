from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from registration.serializers import UserSerializer


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(APIView):
    def post(self, request, format=None):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        confirm_password = request.data['confirm_password']
        
        if confirm_password != password:
            return Response({"content": "Password do not match"}, status.HTTP_400_BAD_REQUEST)
        else:
            User.objects.create_user(username, email, password)
            return Response({}, status.HTTP_200_OK)
