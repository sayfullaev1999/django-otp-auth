from django.urls import path

from core.views import (
    AuthByOTPCodeAPIView,
    SendOtpAPIView
)


urlpatterns = [
    path("send-otp-code/", SendOtpAPIView.as_view(), name="send-otp-code"),
    path("auth/", AuthByOTPCodeAPIView.as_view(), name="auth-by-otp-code"),
]
