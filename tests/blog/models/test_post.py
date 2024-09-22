import pytest

from blog.models import Post, Tag


@pytest.mark.django_db
class TestBlogPost:
    def test_create_post(self, user):
        content = 'some text'
        post = Post.objects.create(author=user, title='Test Title', content=content)

        post_from_db = Post.objects.get(id=post.id)
        assert post_from_db.author == user
        assert post_from_db.title == 'Test Title'
        assert post_from_db.content == content
        assert post_from_db.status == Post.Status.DRAFT
        assert post_from_db.slug == 'test-title'
        assert post_from_db.tags.count() == 0

    def test_add_tags_to_post(self, user):
        post = Post.objects.create(author=user, title='Test Title', content='some text')
        tag1 = Tag.objects.create(name='Test Tag 1')
        tag2 = Tag.objects.create(name='Test Tag 2')
        post.tags.add(tag1, tag2)
        assert post.tags.count() == 2
        assert tag1 in post.tags.all()
        assert tag2 in post.tags.all()

    def test_post_status(self):
        assert Post.Status.choices == [('draft', 'Draft'), ('pub', 'Published')]

    def test_save_slug(self, user):
        post = Post.objects.create(author=user, title='Test Title Sample SLUG', content='some text')
        assert post.slug == 'test-title-sample-slug'
