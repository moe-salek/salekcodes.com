import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestAwardApi:
    def test_list_award(self, award):
        client = APIClient()
        url = reverse('award')
        response = client.get(url)
        assert response.json()[0]['id'] == 1

    def test_retrieve_award(self, award):
        client = APIClient()
        url = reverse('award_detail', kwargs={'id': 1})
        response = client.get(url)
        assert response.json()['id'] == 1
