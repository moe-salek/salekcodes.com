import pytest

from resume_cv.models import Skill


@pytest.mark.django_db
class TestSkillModel:
    model_class = Skill

    def test_model_create(self):
        required_kwargs = {'name': 'test skill'}
        assert self.model_class.objects.count() == 0
        created_instance = self.model_class.objects.create(**required_kwargs)
        assert self.model_class.objects.get() == created_instance
