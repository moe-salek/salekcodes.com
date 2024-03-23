import json
from datetime import datetime

import pytest
import pytz
from django.contrib.auth import get_user_model

from blog.models import Post, Tag
from resume_cv.models import Award, Certificate, Contact, Education, Experience, ResumeCV, Skill

#  region core:


@pytest.fixture
def user_kwargs():
    yield {
        'email': 'test@salekcodes.com',
        'password': 'TestPassword123$%^',  # pragma: allowlist secret
    }


@pytest.fixture
def user(user_kwargs):
    yield get_user_model().objects.create_user(email=user_kwargs['email'], password=user_kwargs['password'])


# endregion

# region blog:


@pytest.fixture
def tag_kwargs():
    yield {'name': 'test_tag'}


@pytest.fixture
def tag(tag_kwargs):
    yield Tag.objects.create(**tag_kwargs)


@pytest.fixture
def post_kwargs(user):
    yield {'author': user, 'title': 'Test Title', 'content': json.dumps({'delta': 'test', 'html': '<p>test</p>'})}


@pytest.fixture
def post(post_kwargs, tag):
    post = Post.objects.create(**post_kwargs)
    post.tags.add(tag)
    yield post


# endregion

# region resume_cv


@pytest.fixture
def skill_kwargs():
    yield {'name': 'test name', 'description': 'test desc'}


@pytest.fixture
def skill(skill_kwargs):
    yield Skill.objects.create(**skill_kwargs)


@pytest.fixture
def experience_kwargs():
    yield {
        'company_name': 'test company name',
        'job_title': 'test job title',
        'description': 'test desc',
        'start_at': datetime(2023, 1, 1, tzinfo=pytz.utc),
        'end_at': datetime(2024, 1, 1, tzinfo=pytz.utc),
        'url': 'https://salekcodes.com',
    }


@pytest.fixture
def experience(experience_kwargs):
    yield Experience.objects.create(**experience_kwargs)


@pytest.fixture
def education_kwargs():
    yield {
        'organization_name': 'test organization',
        'degree': 'test degree',
        'major': 'test major',
        'description': 'test desc',
        'start_at': datetime(2023, 1, 1, tzinfo=pytz.utc),
        'end_at': datetime(2024, 1, 1, tzinfo=pytz.utc),
    }


@pytest.fixture
def education(education_kwargs):
    yield Education.objects.create(**education_kwargs)


@pytest.fixture
def certificate_kwargs():
    yield {
        'title': 'test title',
        'description': 'test desc',
        'issuer': 'test issuer',
        'issued_at': datetime(2023, 1, 1, tzinfo=pytz.utc),
        'expire_at': datetime(2024, 1, 1, tzinfo=pytz.utc),
        'url': 'https://salekcodes.com',
    }


@pytest.fixture
def certificate(certificate_kwargs):
    yield Certificate.objects.create(**certificate_kwargs)


@pytest.fixture
def award_kwargs():
    yield {'title': 'test title', 'description': 'test desc', 'issued_at': datetime(2024, 1, 1, tzinfo=pytz.utc)}


@pytest.fixture
def award(award_kwargs):
    yield Award.objects.create(**award_kwargs)


@pytest.fixture
def contact_kwargs():
    yield {
        'email': 'test@salekcodes.com',
        'phone': '+12345678901',
        'website': 'https://salekcodes.com',
        'github': 'https://github.com/mohammadsalek/',
        'linkedin': 'http://linkedin.com/in/mohammad-salek/',
    }


@pytest.fixture
def contact(contact_kwargs):
    yield Contact.objects.create(**contact_kwargs)


@pytest.fixture
def resume_cv_kwargs(user, contact):
    yield {
        'user': user,
        'title': 'test title',
        'summary': 'test summary',
        'contact': contact,
        'version': 2,
        'is_public': True,
    }


@pytest.fixture
def resume_cv(resume_cv_kwargs):
    yield ResumeCV.objects.create(**resume_cv_kwargs)


# endregion
