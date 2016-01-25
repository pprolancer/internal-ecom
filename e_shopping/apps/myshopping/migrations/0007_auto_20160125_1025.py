# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshopping', '0006_auto_20160125_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='user',
        ),
        migrations.DeleteModel(
            name='ShoppingCart',
        ),
    ]
