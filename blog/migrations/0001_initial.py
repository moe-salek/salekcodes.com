# Generated by Django 5.1.1 on 2024-09-22 02:20

import blog.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', blog.models.AutoDateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={'abstract': False},
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', blog.models.AutoDateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=5000)),
                (
                    'status',
                    models.CharField(choices=[('draft', 'Draft'), ('pub', 'Published')], default='draft', max_length=5),
                ),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                (
                    'author',
                    models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
                ),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='blog.tag')),
            ],
            options={'abstract': False},
        ),
    ]
