from typing import Any, Self

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

from core.validators import validate_email, validate_password


# region user


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


# endregion


# region base


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class Base(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = AutoDateTimeField(default=timezone.now)

    class Meta:
        abstract = True


# endregion


class Social(Base):
    obfuscated_email = models.CharField(max_length=255, default='salek‌[‌dot‌]mo‌e[‌at‌]‌g‌ma‌‌i‌‌l')
    github_url = models.URLField(default='https://github.com/moe-salek/')
    linkedin_url = models.URLField(default='https://www.linkedin.com/in/moe-salek/')
    instagram_url = models.URLField(default='')
    telegram_url = models.URLField(default='')
    x_url = models.URLField(default='')
