from typing import Any, Self

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from core.validators import validate_email, validate_password


class UserManager(BaseUserManager):
    def create_user(self: Self, email: str, password: str, **extra_fields: dict[str, Any]):
        # validate:
        validate_email(email)
        validate_password(password)
        # create user:
        normalized_email = self.normalize_email(email)
        user = self.model(email=normalized_email, **extra_fields)
        user.set_password(password)  # type: ignore[attr-defined]
        user.save(using=self._db)

        return user

    def create_superuser(self: Self, email: str, password: str, **extra_fields: dict[str, Any]):
        # create normal user:
        user = self.create_user(email, password, **extra_fields)
        # make it superuser:
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, default='', null=False, blank=True)
    last_name = models.CharField(max_length=255, default='', null=False, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # username, email and password is required by default

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'
