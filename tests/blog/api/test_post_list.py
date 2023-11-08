import pytest
from django.urls import reverse

from blog.models import Post
from blog.serializers import (
    AuthorSerializer,
    ContentSerializer,
    PostSerializer,
    TagSerializer,
)
from blog.views import PostListView


@pytest.mark.django_db
class TestPostList:
    def test_api_method(self, client):
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
        assert PostListView.serializer_class == PostSerializer

    def test_queryset(self):
        assert PostListView.queryset.model == Post

    def test_get(self, client, post):
        response = client.get(reverse('post_list'))
        assert response.status_code == 200

        response = response.json()[0]
        assert response['id'] == post.id
        assert response['title'] == post.title
        assert response['slug'] == post.slug
        assert response['status'] == post.status.lower()
        assert response['author'] == dict(AuthorSerializer(post.author).data)
        assert response['content'] == dict(ContentSerializer(post.content).data)
        assert response['tags'] == list(TagSerializer(post.tags, many=True).data)
        assert 'created_at' in response
        assert 'modified_at' in response
