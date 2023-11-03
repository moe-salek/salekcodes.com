from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# region abstract/base


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class Base(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = AutoDateTimeField(default=timezone.now)

    class Meta:
        abstract = True


# endregion


class Post(Base):
    class Status(models.TextChoices):
        DRAFT = 'dft', 'Draft'
        PUBLISHED = 'psh', 'Published'

    author = models.ForeignKey(get_user_model(), on_delete=models.RESTRICT)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField('blog.Tag', related_name='posts')
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.DRAFT)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Tag(Base):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.name
