# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-06 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160204_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]