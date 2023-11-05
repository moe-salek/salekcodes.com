import json

import pytest

from blog.models import Post, Tag


@pytest.mark.django_db
class TestBlogPost:
    quill_content = json.dumps({'delta': 'test', 'html': '<p>test</p>'})

    def test_create_post(self, user):
        quill_content = self.quill_content
        post = Post.objects.create(
            author=user,
            title='Test Title',
            content=quill_content,
        )

        post_from_db = Post.objects.get(id=post.id)
        assert post_from_db.author == user
        assert post_from_db.title == 'Test Title'
        assert post_from_db.content.plain == 'test'
        assert post_from_db.status == Post.Status.DRAFT
        assert post_from_db.slug == 'test-title'
        assert post_from_db.tags.count() == 0

    def test_add_tags_to_post(self, user):
        post = Post.objects.create(
            author=user,
            title='Test Title',
            content=self.quill_content,
        )
        tag1 = Tag.objects.create(name='Test Tag 1')
        tag2 = Tag.objects.create(name='Test Tag 2')
        post.tags.add(tag1, tag2)
        assert post.tags.count() == 2
        assert tag1 in post.tags.all()
        assert tag2 in post.tags.all()

    def test_post_status(self):
        assert Post.Status.choices == [
            ('dft', 'Draft'),
            ('psh', 'Published'),
        ]

    def test_save_slug(self, user):
        post = Post.objects.create(
            author=user,
            title='Test Title Sample SLUG',
            content=self.quill_content,
        )
        assert post.slug == 'test-title-sample-slug'
