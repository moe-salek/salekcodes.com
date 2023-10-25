import pytest
from django.core.exceptions import ValidationError

from core.validators import validate_password


@pytest.mark.django_db
class TestCoreCustomValidators:
    @pytest.mark.parametrize(
        'invalid_password',
        [
            0,
            12345,
            1234567890,
            0.0,
            1234567890.0123456789,
            None,
            False,
            True,
            '',
            ' ',
            'passpassword',
            'Password',
            'PASSWORD',
            'Password1234567890',
            'password12345678!@#$%^&*',
            set(),
            {},
            [],
            'qwertyuiopasdfghjklzxcvbnm',  # pragma: allowlist secret
            'QWERTYUIOPASDFGHJKLZXCVBNM',  # pragma: allowlist secret
        ],
    )
    def test_validate_password_invalid(self, invalid_password):
        with pytest.raises(ValidationError) as err:
            validate_password(invalid_password)

        expected_err_msg = [
            'Password must be at least 8 characters long, contain at least one uppercase letter, '
            'one lowercase letter, one digit, and one special character'
        ]
        assert str(err.value) == str(expected_err_msg)

    def test_validate_password_valid(self):
        password = 'Test1234!'  # pragma: allowlist secret

        assert len(password) >= 8
        assert any(char.isupper() for char in password)
        assert any(char.islower() for char in password)
        assert any(char.isdigit() for char in password)
        assert any(char in '!@#$%^&*()+?.|\\' for char in password)

        validate_password(password)


# TODO: add email validator tests
