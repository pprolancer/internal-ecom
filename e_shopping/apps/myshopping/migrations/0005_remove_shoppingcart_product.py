# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshopping', '0004_shoppingcart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='product',
        ),
    ]
