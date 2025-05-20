from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import *

from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from .models import OTP


# Create your views here.

User = get_user_model()


class LoginView(APIView):
    @swagger_auto_schema(methods = ['POST'], request_body=LoginSerializer())
    @action(detail=True, methods=['POST'])

    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request,
            email = serializer.validated_data.get('email'),
            password = serializer.validated_data.get('password')
        )

        if user:

            token_data = RefreshToken.for_user(user)

            data = {
                "name": user.full_name,
                "role": user.role,
                "refresh": str(token_data),
                "access": str(token_data.access_token)
            }

            return Response(data, status=200)
        
        return Response({"error": "Invalid credentials"}, status=400)




class UserGenericView(generics.ListCreateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]



    def create(self, request, *args, **kwargs):

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        User.objects.create_user(
            **serializer._validated_data
        )


        return Response(serializer.data, status=201)

    def list(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return Response({'error': 'Authentication credentials not valid'}, status=403)

        users = User.objects.all()

        return Response(UserSerializer(users, many=True).data, status=200)
    

class UserGenericByOne(generics.RetrieveAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'pk'


class OtpVerifyView(APIView):
    @swagger_auto_schema(methods = ['POST'], request_body=OtpSerializer())
    @action(detail=True, methods = ['POST']) 

    def post(self, request):

        serializer = OtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        otp = serializer.validated_data['otp']

        if not OTP.objects.filter(otp=otp).exists():
            return Response({'error': 'Invalid OTP'}, status=404)
        
        otp = OTP.objects.get(otp=otp)

        if otp.is_otp_valid():
            
            otp.user.is_active = True
            otp.user.save()

            otp.delete()

            return Response({'message': 'OTP verified successfully'}, status=200)
        
        else:

            otp.delete()

            return Response({'error': 'OTP expired'}, status=400)


      






