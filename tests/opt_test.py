import json
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from core.models import User
from core.service import OtpService

pytestmark = pytest.mark.django_db


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def test_user():
    return User.objects.create(email="test@example.com", phone="+1234567890")


@pytest.fixture
def otp_service():
    return OtpService(email_or_phone="+1234567890")


def test_generate_otp(otp_service: OtpService):
    otp_service.generate()
    otp_data = json.loads(otp_service.file_service.read_or_create(OtpService.FILE_NAME))
    assert "+1234567890" in otp_data
    assert "code" in otp_data["+1234567890"]
    assert "expire" in otp_data["+1234567890"]


def test_check_otp_valid(otp_service: OtpService):
    otp_service.generate()
    otp_data = json.loads(otp_service.file_service.read_or_create(OtpService.FILE_NAME))
    otp_code = otp_data["+1234567890"]["code"]
    assert otp_service.check(otp_code) is True


def test_check_otp_invalid(otp_service):
    otp_service.generate()
    assert otp_service.check("123456") is False


def test_send_otp_api(api_client):
    url = reverse("send-otp-code")
    response = api_client.post(url, {"phone": "+1234567890"})
    assert response.status_code == 201
    assert response.json()["status"] == "OK"
