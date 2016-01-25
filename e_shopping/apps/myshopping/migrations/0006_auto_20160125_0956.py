# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myshopping', '0005_remove_shoppingcart_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='user_product_price_limit',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], default=0),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='user_productcount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
