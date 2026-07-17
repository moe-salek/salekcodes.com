import pytest

from blog.models import Post
from blog.views import ARCHIVE_PAGE_SIZE, ECHOES_PAGE_SIZE


def create_published_posts(user, count: int) -> list[Post]:
    return [
        Post.objects.create(author=user, title=f'Echo {i}', content=f'body {i}', status=Post.Status.PUBLISHED)
        for i in range(count)
    ]


@pytest.mark.django_db
class TestEchoes:
    def test_returns_200(self, client):
        assert client.get('/echoes/').status_code == 200

    def test_empty_state_without_posts(self, client):
        assert b'Nothing echoing here yet' in client.get('/echoes/').content

    def test_shows_published_hides_draft(self, client, published_post, post):
        body = client.get('/echoes/').content.decode()
        assert published_post.get_absolute_url() in body
        assert post.get_absolute_url() not in body

    def test_limited_to_page_size(self, client, user):
        create_published_posts(user, ECHOES_PAGE_SIZE + 3)
        body = client.get('/echoes/').content.decode()
        assert body.count('echo-entry__timestamp-link') == ECHOES_PAGE_SIZE


@pytest.mark.django_db
class TestEchoesArchive:
    def test_returns_200_with_empty_state(self, client):
        response = client.get('/echoes/archive/')
        assert response.status_code == 200
        assert b'Nothing echoing here yet' in response.content

    def test_paginates(self, client, user):
        create_published_posts(user, ARCHIVE_PAGE_SIZE + 5)

        first = client.get('/echoes/archive/').content.decode()
        assert first.count('echo-entry__timestamp-link') == ARCHIVE_PAGE_SIZE
        assert 'Page 1 of 2' in first
        assert '?page=2' in first

        second = client.get('/echoes/archive/?page=2').content.decode()
        assert second.count('echo-entry__timestamp-link') == 5
        assert '?page=1' in second

    def test_out_of_range_page_clamps(self, client, user):
        create_published_posts(user, 3)
        response = client.get('/echoes/archive/?page=99')
        assert response.status_code == 200
        assert response.content.decode().count('echo-entry__timestamp-link') == 3

    def test_no_pagination_nav_for_single_page(self, client, published_post):
        assert 'Page 1 of' not in client.get('/echoes/archive/').content.decode()


@pytest.mark.django_db
class TestEchoUniquePage:
    def test_published_by_slug(self, client, published_post):
        response = client.get(published_post.get_absolute_url())
        assert response.status_code == 200
        assert published_post.title in response.content.decode()

    def test_draft_404(self, client, post):
        assert client.get(post.get_absolute_url()).status_code == 404

    def test_unknown_slug_404(self, client):
        assert client.get('/echoes/no-such-echo/').status_code == 404

    def test_legacy_id_redirects_to_slug(self, client, published_post):
        response = client.get(f'/echoes/{published_post.id}/')
        assert response.status_code == 301
        assert response['Location'] == published_post.get_absolute_url()

    def test_meta_description_from_content(self, client, published_post):
        body = client.get(published_post.get_absolute_url()).content.decode()
        assert '<meta name="description" content="A published echo.' in body
        assert '<meta property="og:type" content="article" />' in body


@pytest.mark.django_db
class TestMarkdownSanitization:
    def test_script_tags_stripped(self, client, user):
        post = Post.objects.create(
            author=user,
            title='Evil Echo',
            content='hello <script>alert(1)</script> world',
            status=Post.Status.PUBLISHED,
        )
        body = client.get(post.get_absolute_url()).content.decode()
        assert '<script>alert(1)</script>' not in body

    def test_code_highlighting_survives(self, client, user):
        post = Post.objects.create(
            author=user,
            title='Code Echo',
            content='```python\nprint(1)\n```',
            status=Post.Status.PUBLISHED,
        )
        body = client.get(post.get_absolute_url()).content.decode()
        assert 'class="codehilite"' in body


@pytest.mark.django_db
class TestEchoesByTag:
    def test_lists_only_tagged_published_posts(self, client, user, tag, published_post, post):
        untagged = Post.objects.create(author=user, title='Untagged', content='body', status=Post.Status.PUBLISHED)
        body = client.get(f'/echoes/tag/{tag.name}/').content.decode()
        assert published_post.get_absolute_url() in body
        assert untagged.get_absolute_url() not in body
        assert post.get_absolute_url() not in body  # draft, even though tagged

    def test_unknown_tag_404(self, client):
        assert client.get('/echoes/tag/no-such-tag/').status_code == 404

    def test_empty_state(self, client, tag):
        response = client.get(f'/echoes/tag/{tag.name}/')
        assert response.status_code == 200
        assert b'No echoes carry this tag yet' in response.content

    def test_tag_feed_lists_only_tagged(self, client, user, tag, published_post):
        untagged = Post.objects.create(author=user, title='Untagged', content='body', status=Post.Status.PUBLISHED)
        response = client.get(f'/echoes/tag/{tag.name}/feed/')
        body = response.content.decode()
        assert response.status_code == 200
        assert published_post.title in body
        assert untagged.title not in body
        assert f'#{tag.name}' in body

    def test_tag_feed_unknown_tag_404(self, client):
        assert client.get('/echoes/tag/no-such-tag/feed/').status_code == 404

    def test_entry_tags_link_to_tag_page(self, client, published_post, tag):
        body = client.get('/echoes/').content.decode()
        assert f'href="/echoes/tag/{tag.name}/"' in body


@pytest.mark.django_db
class TestEchoesSearch:
    def test_no_query_shows_prompt(self, client):
        response = client.get('/echoes/search/')
        assert response.status_code == 200
        assert b'Type something above to search' in response.content

    def test_matches_title_and_content(self, client, user):
        by_title = Post.objects.create(
            author=user, title='Needle Title', content='body', status=Post.Status.PUBLISHED
        )
        by_content = Post.objects.create(
            author=user, title='Other', content='a needle in the body', status=Post.Status.PUBLISHED
        )
        miss = Post.objects.create(author=user, title='Hay', content='only hay', status=Post.Status.PUBLISHED)

        body = client.get('/echoes/search/?q=needle').content.decode()
        assert by_title.get_absolute_url() in body
        assert by_content.get_absolute_url() in body
        assert miss.get_absolute_url() not in body

    def test_excludes_drafts(self, client, post):
        body = client.get('/echoes/search/?q=Test').content.decode()
        assert post.get_absolute_url() not in body

    def test_no_results_message(self, client):
        assert 'No echoes match' in client.get('/echoes/search/?q=zzz-nothing').content.decode()

    def test_pagination_preserves_query(self, client, user):
        for i in range(ARCHIVE_PAGE_SIZE + 1):
            Post.objects.create(
                author=user, title=f'Needle {i}', content='body', status=Post.Status.PUBLISHED
            )
        first = client.get('/echoes/search/?q=needle').content.decode()
        assert '?q=needle&page=2' in first
        second = client.get('/echoes/search/?q=needle&page=2').content.decode()
        assert second.count('echo-entry__timestamp-link') == 1


@pytest.mark.django_db
class TestFeedAndSitemap:
    def test_feed_lists_published(self, client, published_post, post):
        response = client.get('/echoes/feed/')
        body = response.content.decode()
        assert response.status_code == 200
        assert 'rss' in response['Content-Type']
        assert published_post.title in body
        assert post.title not in body

    def test_sitemap_lists_pages_and_echoes(self, client, published_post):
        response = client.get('/sitemap.xml')
        body = response.content.decode()
        assert response.status_code == 200
        assert '/about/' in body
        assert published_post.get_absolute_url() in body
