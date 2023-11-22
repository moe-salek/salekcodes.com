import pytest

from resume_cv.models import Contact


@pytest.mark.django_db
class TestContactModel:
    model_class = Contact

    def test_model_create(self):
        required_kwargs = {
            'email': 'test@email.com',
        }
        assert self.model_class.objects.count() == 0
        created_instance = self.model_class.objects.create(**required_kwargs)
        assert self.model_class.objects.get() == created_instance
