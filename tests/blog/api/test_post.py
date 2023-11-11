import pytest
from django.urls import reverse

from blog.models import Post
from blog.serializers import (
    AuthorSerializer,
    ContentSerializer,
    PostSerializer,
    TagSerializer,
)
from blog.views import PostView


@pytest.mark.django_db
class TestPostList:
    def test_http_method(self, client, post):
        response = client.post(reverse('post_list'))
        assert response.status_code == 405
        response = client.put(reverse('post_list'))
        assert response.status_code == 405
        response = client.patch(reverse('post_list'))
        assert response.status_code == 405
        response = client.delete(reverse('post_list'))
        assert response.status_code == 405
        response = client.get(reverse('post_list'))
        assert response.status_code == 200

    def test_serializer(self):
        assert PostView.serializer_class == PostSerializer

    def test_queryset(self):
        assert PostView.queryset.model == Post

    def test_list(self, client, post):
        response = client.get(reverse('post_list'))
        assert response.status_code == 200

        response = response.json()
        assert isinstance(response, list)
        first_item = response[0]
        assert first_item['id'] == post.id
        assert first_item['title'] == post.title
        assert first_item['slug'] == post.slug
        assert first_item['status'] == post.status.lower()
        assert first_item['author'] == dict(AuthorSerializer(post.author).data)
        assert first_item['content'] == dict(ContentSerializer(post.content).data)
        assert first_item['tags'] == list(TagSerializer(post.tags, many=True).data)
        assert 'created_at' in first_item
        assert 'modified_at' in first_item


@pytest.mark.django_db
class TestPostRetrieve:
    def test_http_method(self, client, post):
        kwargs = {'id': post.id}
        response = client.post(reverse('post_retrieve', kwargs=kwargs))
        assert response.status_code == 405
        response = client.put(reverse('post_retrieve', kwargs=kwargs))
        assert response.status_code == 405
        response = client.patch(reverse('post_retrieve', kwargs=kwargs))
        assert response.status_code == 405
        response = client.delete(reverse('post_retrieve', kwargs=kwargs))
        assert response.status_code == 405
        response = client.get(reverse('post_retrieve', kwargs=kwargs))
        assert response.status_code == 200

    def test_serializer(self):
        assert PostView.serializer_class == PostSerializer

    def test_queryset(self):
        assert PostView.queryset.model == Post

    def test_retrieve(self, client, post):
        kwargs = {'id': post.id}
        response = client.get(reverse('post_retrieve', kwargs=kwargs))
        assert response.status_code == 200

        response = response.json()
        assert response['id'] == post.id
        assert response['title'] == post.title
        assert response['slug'] == post.slug
        assert response['status'] == post.status.lower()
        assert response['author'] == dict(AuthorSerializer(post.author).data)
        assert response['content'] == dict(ContentSerializer(post.content).data)
        assert response['tags'] == list(TagSerializer(post.tags, many=True).data)
        assert 'created_at' in response
        assert 'modified_at' in response
