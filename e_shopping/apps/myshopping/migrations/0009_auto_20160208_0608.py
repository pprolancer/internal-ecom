# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-08 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_birth_date'),
        ('myshopping', '0008_auto_20160205_0909'),
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
        migrations.AddField(
            model_name='cart',
            name='from_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fromuser_cards', to='users.UserProfile'),
        ),
        migrations.AddField(
            model_name='cart',
            name='to_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='touser_cards', to='users.UserProfile'),
        ),
        migrations.AddField(
            model_name='order',
            name='from_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fromuser_orders', to='users.UserProfile'),
        ),
        migrations.AddField(
            model_name='order',
            name='to_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='touser_orders', to='users.UserProfile'),
        ),
    ]
