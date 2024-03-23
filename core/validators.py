from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, RegexValidator


def validate_password(password: str, min_length: int = 8) -> None:
    message = (
        f'Password must be at least {min_length} characters long, contain at least one uppercase letter, '
        'one lowercase letter, one digit, and one special character'
    )
    try:
        if not password or not isinstance(password, str):
            raise ValidationError(message)
        regex = rf'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])[a-zA-Z\d!@#$%^&*()_+]{{{min_length},}}$'
        validator = RegexValidator(regex=regex, message=message)
        validator(password)
    except ValidationError:
        raise ValidationError(message)

    return None


def validate_email(email: str) -> None:
    message = 'Email has invalid format or is empty'
    try:
        if not email or not isinstance(email, str):
            raise ValidationError(message)
        validator = EmailValidator()
        validator(email)
    except ValidationError:
        raise ValidationError(message)

    return None
