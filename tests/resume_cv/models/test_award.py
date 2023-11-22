import pytest

from resume_cv.models import Award


@pytest.mark.django_db
class TestAwardModel:
    model_class = Award

    def test_model_create(self):
        required_kwargs = {
            'title': 'test title',
        }
        assert self.model_class.objects.count() == 0
        created_instance = self.model_class.objects.create(**required_kwargs)
        assert self.model_class.objects.get() == created_instance
