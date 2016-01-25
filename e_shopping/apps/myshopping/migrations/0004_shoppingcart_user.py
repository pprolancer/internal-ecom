# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myshopping', '0003_remove_shoppingcart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(related_name='shoppingcart_user', default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
