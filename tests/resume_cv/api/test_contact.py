import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestContactApi:
    def test_list_contact(self, contact):
        client = APIClient()
        url = reverse('contact')
        response = client.get(url)
        assert response.json()[0]['id'] == 1

    def test_retrieve_contact(self, contact):
        client = APIClient()
        url = reverse('contact_detail', kwargs={'id': 1})
        response = client.get(url)
        assert response.json()['id'] == 1
