import pytest

from resume.models import ResumeCV


@pytest.mark.django_db
class TestResumeCVModel:
    model_class = ResumeCV

    def test_model_create(self, user):
        required_kwargs = {'user': user, 'title': 'test title'}
        assert self.model_class.objects.count() == 0
        created_instance = self.model_class.objects.create(**required_kwargs)
        assert self.model_class.objects.get() == created_instance
