# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshopping', '0009_auto_20160127_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.CharField(verbose_name='Product cart Price', default='', max_length=100),
            preserve_default=False,
        ),
    ]
