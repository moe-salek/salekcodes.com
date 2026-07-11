import pytest
from django.conf import settings


@pytest.mark.django_db
class TestIndex:
    def test_returns_200(self, client):
        assert client.get('/').status_code == 200

    def test_empty_state_without_posts(self, client):
        assert b'Nothing echoing here yet' in client.get('/').content

    def test_shows_published_posts(self, client, published_post):
        body = client.get('/').content.decode()
        assert 'Recent echoes' in body
        assert published_post.get_absolute_url() in body

    def test_hides_drafts(self, client, post):
        assert post.get_absolute_url() not in client.get('/').content.decode()


@pytest.mark.django_db
class TestStaticPages:
    def test_about(self, client):
        response = client.get('/about/')
        assert response.status_code == 200
        assert b'Moe Salek' in response.content

    def test_connect_hides_unset_socials(self, client):
        response = client.get('/connect/')
        body = response.content.decode()
        assert response.status_code == 200
        assert 'GitHub profile' in body
        assert 'LinkedIn profile' in body
        assert 'Instagram profile' not in body
        assert 'X profile' not in body

    def test_coming_soon(self, client):
        assert client.get('/coming-soon/').status_code == 200


@pytest.mark.django_db
class TestRobotsTxt:
    def test_serves_plain_text_rules(self, client):
        response = client.get('/robots.txt')
        body = response.content.decode()
        assert response.status_code == 200
        assert response['Content-Type'].startswith('text/plain')
        assert 'User-agent: *' in body
        assert 'Disallow: /admin/' in body
        assert f'Sitemap: {settings.SITE_URL}/sitemap.xml' in body
