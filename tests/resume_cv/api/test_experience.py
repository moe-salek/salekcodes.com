import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestExperienceApi:
    def test_list_experience(self, experience):
        client = APIClient()
        url = reverse('experience')
        response = client.get(url)
        assert response.json()[0]['id'] == 1

    def test_retrieve_experience(self, experience):
        client = APIClient()
        url = reverse('experience_detail', kwargs={'id': 1})
        response = client.get(url)
        assert response.json()['id'] == 1
