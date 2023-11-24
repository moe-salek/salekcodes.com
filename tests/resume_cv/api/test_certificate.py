import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestCertificateApi:
    def test_list_certificate(self, certificate):
        client = APIClient()
        url = reverse('certificate')
        response = client.get(url)
        assert response.json()[0]['id'] == 1

    def test_retrieve_certificate(self, certificate):
        client = APIClient()
        url = reverse('certificate_detail', kwargs={'id': 1})
        response = client.get(url)
        assert response.json()['id'] == 1
