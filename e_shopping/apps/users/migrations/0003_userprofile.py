# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20160122_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user_role', models.CharField(verbose_name='User Role', max_length=100, db_index=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='profile')),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
    ]
