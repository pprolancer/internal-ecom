# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myshopping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('product_count', models.IntegerField(null=True, blank=True)),
                ('product_price_limit', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('product', models.ForeignKey(to='myshopping.Product', related_name='product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='shoppingcart_user')),
            ],
            options={
                'verbose_name': 'ShoppingCart',
                'verbose_name_plural': 'ShoppingCart',
            },
        ),
    ]
