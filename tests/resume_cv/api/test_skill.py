import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestSkillApi:
    def test_list_skill(self, skill):
        client = APIClient()
        url = reverse('skill')
        response = client.get(url)
        assert response.json()[0]['id'] == 1

    def test_retrieve_skill(self, skill):
        client = APIClient()
        url = reverse('skill_detail', kwargs={'id': 1})
        response = client.get(url)
        assert response.json()['id'] == 1
