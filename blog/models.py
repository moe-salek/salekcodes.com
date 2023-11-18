from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django_quill.fields import QuillField

from salekcodes.models import Base


class Post(Base):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'pub', 'Published'

    author = models.ForeignKey(get_user_model(), on_delete=models.RESTRICT)
    title = models.CharField(max_length=255)
    content = QuillField()
    tags = models.ManyToManyField('blog.Tag', related_name='posts', blank=True)
    status = models.CharField(max_length=5, choices=Status.choices, default=Status.DRAFT)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Tag(Base):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.name
