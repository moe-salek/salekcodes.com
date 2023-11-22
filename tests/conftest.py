import json

import pytest
from django.contrib.auth import get_user_model

from blog.models import Post, Tag

#  region core:


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


# endregion

# region blog:


@pytest.fixture
def tag_kwargs():
    yield {'name': 'test_tag'}


@pytest.fixture
@pytest.mark.django_db
def tag(tag_kwargs):
    yield Tag.objects.create(**tag_kwargs)


@pytest.fixture
@pytest.mark.django_db
def post_kwargs(user):
    yield {
        'author': user,
        'title': 'Test Title',
        'content': json.dumps({'delta': 'test', 'html': '<p>test</p>'}),
    }


@pytest.fixture
@pytest.mark.django_db
def post(post_kwargs, tag):
    post = Post.objects.create(**post_kwargs)
    post.tags.add(tag)
    yield post


# endregion

# region resume_cv

# endregion
