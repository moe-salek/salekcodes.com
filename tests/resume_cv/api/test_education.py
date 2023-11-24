import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestEducationApi:
    def test_list_education(self, education):
        client = APIClient()
        url = reverse('education')
        response = client.get(url)
        assert response.json()[0]['id'] == 1

    def test_retrieve_education(self, education):
        client = APIClient()
        url = reverse('education_detail', kwargs={'id': 1})
        response = client.get(url)
        assert response.json()['id'] == 1
