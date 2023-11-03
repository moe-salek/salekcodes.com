import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def user_kwargs():
    yield {
        'email': 'test@salekcodes.com',
        'password': 'TestPassword123$%^',  # pragma: allowlist secret
    }


@pytest.fixture
@pytest.mark.django_db
def user(user_kwargs):
    yield get_user_model().objects.create_user(
        email=user_kwargs['email'],
        password=user_kwargs['password'],
    )
