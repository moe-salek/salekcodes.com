import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

import core.models


@pytest.mark.django_db
class TestCoreUser:
    user = get_user_model()
    email = 'test@salekcodes.com'
    password = 'TestPassword123$%^'  # pragma: allowlist secret

    def test_get_user_model_is_core_user(self):
        assert self.user is core.models.User

    def test_create_user_no_args_fail(self):
        assert self.user.objects.exists() is False
        kwargs = {}
        with pytest.raises(TypeError) as err:
            self.user.objects.create_user(**kwargs)
        expected_error_message = (
            "UserManager.create_user() missing 2 required positional arguments: 'email' and 'password'"
        )
        assert str(err.value) == expected_error_message
        assert self.user.objects.exists() is False

    @pytest.mark.parametrize(
        'email',
        [
            None,
            False,
            True,
            '',
            ' ',
            'test',
            'test@',
            '@test',
            '@test.com',
            'test@test',
            'test@test.',
            'test.com',
            0,
            123,
            123.456,
            {},
            [],
            set(),
        ],
    )
    def test_create_user_email_invalid_fail(self, email):
        assert self.user.objects.exists() is False
        kwargs = {
            'email': email,
            'password': self.password,
        }
        with pytest.raises(ValidationError) as err:
            self.user.objects.create_user(**kwargs)
        expected_error_message = ['Email has invalid format or is empty']
        assert str(err.value) == str(expected_error_message)
        assert self.user.objects.exists() is False

    @pytest.mark.parametrize(
        'password',
        [
            None,
            '',
            ' ',
            'test',
            'testtest',
            'testtesttesttest',
            '12345678',
            'test12345678',
            '!@#$%^',
            'Test1234567890',
            'TEST1234567!@#$$',
            'test1234567!@#$$',
            '1234567!@#$$',
            'Test1!',
            '1@Test',
            '!@#$%^&*()',
            0,
            123,
            1234567890,
            123.456,
            123456.789012,
            False,
            True,
            {},
            [],
            set(),
        ],
    )
    def test_create_user_password_invalid_fail(self, password):
        assert self.user.objects.exists() is False
        kwargs = {
            'email': self.email,
            'password': password,
        }
        with pytest.raises(ValidationError) as err:
            self.user.objects.create_user(**kwargs)
        expected_error_message = [
            'Password must be at least 8 characters long, contain at least one uppercase letter, '
            'one lowercase letter, one digit, and one special character'
        ]
        assert str(err.value) == str(expected_error_message)
        assert self.user.objects.exists() is False

    def test_create_user_valid(self):
        assert self.user.objects.exists() is False
        kwargs = {
            'email': self.email,
            'password': self.password,
        }
        created_user = self.user.objects.create_user(**kwargs)
        assert self.user.objects.exists() is True
        assert self.user.objects.count() == 1
        assert self.user.objects.get() == created_user
        assert created_user.email == self.email
        assert created_user.check_password(self.password) is True
        assert created_user.is_active is True
        assert created_user.is_staff is False
        assert created_user.is_superuser is False
        assert created_user.first_name == ''
        assert created_user.last_name == ''

    def test_user_fields(self):
        expected_user_fields = ['email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
        for model_field in expected_user_fields:
            assert self.user._meta.get_field(model_field) is not None
        assert self.user.USERNAME_FIELD == 'email'
        assert self.user.REQUIRED_FIELDS == []
        assert isinstance(self.user.objects, core.models.UserManager)

    def test_user_str(self):
        instance = self.user()
        instance.email = self.email
        assert str(instance) == self.email
