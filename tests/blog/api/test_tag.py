import pytest
from django.urls import reverse

from blog.models import Tag
from blog.serializers import TagSerializer, TagWithPostsSerializer
from blog.views import TagView


@pytest.mark.django_db
class TestTagList:
    def test_http_method(self, client, tag):
        response = client.post(reverse('tag_list'))
        assert response.status_code == 405
        response = client.put(reverse('tag_list'))
        assert response.status_code == 405
        response = client.patch(reverse('tag_list'))
        assert response.status_code == 405
        response = client.delete(reverse('tag_list'))
        assert response.status_code == 405
        response = client.get(reverse('tag_list'))
        assert response.status_code == 200

    def test_serializer(self):
        assert TagView.serializer_class == TagSerializer

    def test_queryset(self):
        assert TagView.queryset.model == Tag

    def test_list(self, client, tag):
        response = client.get(reverse('tag_list'))
        assert response.status_code == 200

        response = response.json()
        assert isinstance(response, list)
        first_item = response[0]
        assert first_item['id'] == tag.id
        assert first_item['name'] == tag.name


@pytest.mark.django_db
class TestTagRetrieve:
    def test_http_method(self, client, tag):
        kwargs = {'id': tag.id}
        response = client.post(reverse('tag_detail', kwargs=kwargs))
        assert response.status_code == 405
        response = client.put(reverse('tag_detail', kwargs=kwargs))
        assert response.status_code == 405
        response = client.patch(reverse('tag_detail', kwargs=kwargs))
        assert response.status_code == 405
        response = client.delete(reverse('tag_detail', kwargs=kwargs))
        assert response.status_code == 405
        response = client.get(reverse('tag_detail', kwargs=kwargs))
        assert response.status_code == 200

    def test_serializer(self):
        assert TagView.serializer_class == TagSerializer

    def test_get_serializer_class(self):
        view = TagView()
        view.action = 'retrieve'
        assert view.get_serializer_class() == TagWithPostsSerializer

    def test_queryset(self):
        assert TagView.queryset.model == Tag

    def test_retrieve(self, client, post, tag):
        kwargs = {'id': tag.id}
        response = client.get(reverse('tag_detail', kwargs=kwargs))
        assert response.status_code == 200

        response = response.json()
        assert response['id'] == tag.id
        assert response['name'] == tag.name
        assert response['posts'] == [post.id]
