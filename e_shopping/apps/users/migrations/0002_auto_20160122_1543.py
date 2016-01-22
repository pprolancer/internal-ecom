# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='from_person',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='from_people'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='to_person',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='to_people'),
        ),
        migrations.DeleteModel(
            name='Parents',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
