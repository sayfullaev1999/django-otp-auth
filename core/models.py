from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

from core.validators import phone_number_validator


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_("Email"),
        null=True, unique=True
    )
    phone = models.CharField(
        verbose_name=_("Phone"),
        max_length=20,
        validators=[phone_number_validator],
        null=True, unique=True
    )

    # USERNAME_FIELD = "username"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        self.username = self.email or self.phone
        super().save(*args, **kwargs)

    def __str__(self):
        if self.phone and self.email:
            return f"{self.email} - {self.phone}"
        elif self.phone:
            return self.phone
        return self.email

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
