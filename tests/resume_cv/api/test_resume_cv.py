import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestResumeCVApi:
    def test_list_resume_cv(self, resume_cv):
        client = APIClient()
        url = reverse('resume_cv')
        response = client.get(url)
        assert response.json()[0]['id'] == 1

    def test_retrieve_resume_cv(self, resume_cv):
        client = APIClient()
        url = reverse('resume_cv_detail', kwargs={'id': 1})
        response = client.get(url)
        assert response.json()['id'] == 1
