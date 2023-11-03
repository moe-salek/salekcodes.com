import pytest
from django.db import IntegrityError

from blog.models import Tag


@pytest.mark.django_db
class TestBlogTag:
    def test_create(self):
        tag = Tag.objects.create(name='Test Tag')
        assert tag.name == 'Test Tag'
        assert Tag.objects.get() == tag

    def test_str(self):
        tag = Tag(name='Test Tag')
        assert str(tag) == 'Test Tag'

    def test_unique_name(self):
        Tag.objects.create(name='Test Tag')
        with pytest.raises(IntegrityError) as err_info:
            Tag.objects.create(name='Test Tag')
        assert str(err_info.value) == 'UNIQUE constraint failed: blog_tag.name'
