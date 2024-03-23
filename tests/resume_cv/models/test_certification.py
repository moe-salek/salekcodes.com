import pytest

from resume.models import Certificate


@pytest.mark.django_db
class TestCertificateModel:
    model_class = Certificate

    def test_model_create(self):
        required_kwargs = {'title': 'test title'}
        assert self.model_class.objects.count() == 0
        created_instance = self.model_class.objects.create(**required_kwargs)
        assert self.model_class.objects.get() == created_instance
