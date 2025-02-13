import json
import time
import random
from typing import Dict


class FileService:
    @staticmethod
    def write(file_path, content: str) -> None:
        with open(file_path, "w") as f:
            f.write(content)

    @staticmethod
    def read_or_create(file_path):
        try:
            with open(file_path, "r") as f:
                return f.read()
        except FileNotFoundError:
            with open(file_path, "w") as f:
                f.write(json.dumps({}))
                return '{}'


class OtpService:
    FILE_NAME = "otp.json"
    CODE_LENGTH = 6
    CODE_LIFETIME = 300  # seconds

    def __init__(self, email_or_phone: str):
        self.email_or_phone = email_or_phone
        self.file_service = FileService()

    def generate(self):
        code = random.randint(10 ** (self.CODE_LENGTH - 1), 10 ** self.CODE_LENGTH - 1)
        otp_codes: Dict[str, Dict[str, int]] = json.loads(self.file_service.read_or_create(self.FILE_NAME))
        otp_codes[self.email_or_phone] = {
            "code": code,
            "expire": int(time.time() * 1000) + int(self.CODE_LIFETIME * 1000)
        }
        self.file_service.write(self.FILE_NAME, json.dumps(otp_codes))

    def check(self, code):
        otp_codes = json.loads(self.file_service.read_or_create(self.FILE_NAME))
        if (
            self.email_or_phone in otp_codes and
            int(time.time() * 1000) <= otp_codes[self.email_or_phone]["expire"]
        ):
            is_verified = otp_codes[self.email_or_phone]["code"] == int(code)
            if is_verified:
                # В случае успешной валидации удаляем однарозовый пароль из файла
                otp_codes.pop(self.email_or_phone)
                self.file_service.write(self.FILE_NAME, json.dumps(otp_codes))
            return is_verified
        return False
