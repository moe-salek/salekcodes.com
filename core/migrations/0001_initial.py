# Generated by Django 5.0.6 on 2024-06-07 19:06

import core.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [('auth', '0012_alter_user_first_name_max_length')]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', core.models.AutoDateTimeField(default=django.utils.timezone.now)),
                (
                    'obfuscated_email',
                    models.CharField(
                        default='salek\u200c[\u200cdot\u200c]mo\u200ce[\u200cat\u200c]\u200cg\u200cma\u200c\u200ci\u200c\u200cl',
                        max_length=255,
                    ),
                ),
                ('github_url', models.URLField(default='https://github.com/MohammadSalek/')),
                ('linkedin_url', models.URLField(default='https://www.linkedin.com/in/moe-salek/')),
                ('instagram_url', models.URLField(default='')),
                ('telegram_url', models.URLField(default='')),
                ('x_url', models.URLField(default='')),
            ],
            options={'abstract': False},
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(blank=True, default='', max_length=255)),
                ('last_name', models.CharField(blank=True, default='', max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                (
                    'groups',
                    models.ManyToManyField(
                        blank=True,
                        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.group',
                        verbose_name='groups',
                    ),
                ),
                (
                    'user_permissions',
                    models.ManyToManyField(
                        blank=True,
                        help_text='Specific permissions for this user.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.permission',
                        verbose_name='user permissions',
                    ),
                ),
            ],
            options={'abstract': False},
        ),
    ]
