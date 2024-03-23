from datetime import datetime

import pytest
import pytz

from resume.models import Experience


@pytest.mark.django_db
class TestExperienceModel:
    model_class = Experience

    def test_model_create(self):
        required_kwargs = {
            'company_name': 'test company',
            'job_title': 'test job title',
            'start_at': datetime(2023, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
        }
        assert self.model_class.objects.count() == 0
        created_instance = self.model_class.objects.create(**required_kwargs)
        assert self.model_class.objects.get() == created_instance
