from datetime import datetime

import pytest
import pytz

from resume_cv.models import Education


@pytest.mark.django_db
class TestEducationModel:
    model_class = Education

    def test_model_create(self):
        required_kwargs = {
            'organization_name': 'test organization',
            'degree': 'test degree',
            'major': 'test major',
            'start_at': datetime(2023, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
        }
        assert self.model_class.objects.count() == 0
        created_instance = self.model_class.objects.create(**required_kwargs)
        assert self.model_class.objects.get() == created_instance
