# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-05 09:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshopping', '0006_auto_20160204_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]