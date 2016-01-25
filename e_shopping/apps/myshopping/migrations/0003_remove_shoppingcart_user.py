# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshopping', '0002_shoppingcart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='user',
        ),
    ]
