# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='product_count',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='product_price_limit',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], default=0),
        ),
    ]
