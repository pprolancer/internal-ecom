# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshopping', '0007_auto_20160125_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('checked_out', models.BooleanField(verbose_name='Checkout', default=False)),
                ('quantity', models.CharField(verbose_name='Quantity', max_length=100)),
                ('product', models.ForeignKey(to='myshopping.Product', related_name='productcart')),
            ],
            options={
                'verbose_name_plural': 'carts',
                'verbose_name': 'cart',
            },
        ),
    ]
