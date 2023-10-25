import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

import core.models


@pytest.mark.django_db
class TestCoreUser:
    email = 'test@salekcodes.com'
    password = 'TestPassword123$%^'  # pragma: allowlist secret

    def test_get_user_model_is_core_user(self):
        assert get_user_model() is core.models.User

    def test_create_user_no_args_fail(self):
        assert get_user_model().objects.exists() is False
        kwargs = {}
        with pytest.raises(TypeError) as err:
            get_user_model().objects.create_user(**kwargs)
        expected_error_message = (
            "UserManager.create_user() missing 2 required positional arguments: 'email' and 'password'"
        )
        assert str(err.value) == expected_error_message
        assert get_user_model().objects.exists() is False

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
        assert get_user_model().objects.exists() is False
        kwargs = {
            'email': email,
            'password': self.password,
        }
        with pytest.raises(ValidationError) as err:
            get_user_model().objects.create_user(**kwargs)
        expected_error_message = ['Email has invalid format or is empty']
        assert str(err.value) == str(expected_error_message)
        assert get_user_model().objects.exists() is False

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
        assert get_user_model().objects.exists() is False
        kwargs = {
            'email': self.email,
            'password': password,
        }
        with pytest.raises(ValidationError) as err:
            get_user_model().objects.create_user(**kwargs)
        expected_error_message = [
            'Password must be at least 8 characters long, contain at least one uppercase letter, '
            'one lowercase letter, one digit, and one special character'
        ]
        assert str(err.value) == str(expected_error_message)
        assert get_user_model().objects.exists() is False

    def test_create_user_valid(self):
        assert get_user_model().objects.exists() is False
        kwargs = {
            'email': self.email,
            'password': self.password,
        }
        created_user = get_user_model().objects.create_user(**kwargs)
        assert get_user_model().objects.exists() is True
        assert get_user_model().objects.count() == 1
        assert get_user_model().objects.get() == created_user
        assert created_user.email == self.email
        assert created_user.check_password(self.password) is True
        assert created_user.is_active is True
        assert created_user.is_staff is False
        assert created_user.is_superuser is False
        assert created_user.first_name == ''
        assert created_user.last_name == ''
