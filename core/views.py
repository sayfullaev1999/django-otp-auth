from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import (
    AuthByOTPCodeSerializer,
    OtpSerializer
)
from .service import OtpService


class SendOtpAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = OtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        OtpService(email_or_phone=serializer.email_or_phone).generate()
        return Response(data={"status": "OK"}, status=status.HTTP_201_CREATED)


class AuthByOTPCodeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthByOTPCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user: User = serializer.save()
        return Response(data=user.tokens, status=status.HTTP_200_OK)
