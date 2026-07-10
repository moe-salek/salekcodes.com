from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from core.models import AutoDateTimeField, Base  # noqa: F401 (AutoDateTimeField kept importable for migrations)


class Post(Base):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'pub', 'Published'

    author = models.ForeignKey(get_user_model(), on_delete=models.RESTRICT)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=5000)
    tags = models.ManyToManyField('blog.Tag', related_name='posts', blank=True)
    status = models.CharField(max_length=5, choices=Status.choices, default=Status.DRAFT)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self) -> str:
        base = slugify(self.title) or 'echo'
        slug = base
        suffix = 2
        while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f'{base}-{suffix}'
            suffix += 1
        return slug

    def __str__(self):
        return self.title


class Tag(Base):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.name
