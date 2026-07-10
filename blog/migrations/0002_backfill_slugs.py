from django.db import migrations
from django.utils.text import slugify


def backfill_slugs(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    taken = set(Post.objects.exclude(slug='').values_list('slug', flat=True))
    for post in Post.objects.filter(slug=''):
        base = slugify(post.title) or 'echo'
        slug = base
        suffix = 2
        while slug in taken:
            slug = f'{base}-{suffix}'
            suffix += 1
        taken.add(slug)
        post.slug = slug
        post.save(update_fields=['slug'])


class Migration(migrations.Migration):
    dependencies = [('blog', '0001_initial')]

    operations = [migrations.RunPython(backfill_slugs, migrations.RunPython.noop)]
