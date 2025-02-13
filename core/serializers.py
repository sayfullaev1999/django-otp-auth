from rest_framework import serializers

from core.models import User
from core.service import OtpService
from core.validators import phone_number_validator


class OtpSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(required=False, validators=[phone_number_validator])

    def validate(self, attrs):
        if attrs.get("email") is None and attrs.get("phone") is None:
            raise serializers.ValidationError({"detail": "Either email or phone is required"})
        return attrs

    @property
    def email_or_phone(self):
        return self.validated_data.get("email") or self.validated_data.get("phone")


class AuthByOTPCodeSerializer(OtpSerializer):
    otp_code = serializers.CharField(required=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        email_or_phone = attrs.get("email") or attrs.get("phone")
        is_verified = OtpService(email_or_phone=email_or_phone).check(attrs["otp_code"])
        if not is_verified:
            raise serializers.ValidationError({"detail": "OTP code verification failed"})
        return attrs

    def create(self, validated_data):
        validated_data.pop("otp_code")
        instance, _ = User.objects.get_or_create(
            email=validated_data.get("email"),
            phone=validated_data.get("phone"),
        )
        return instance
