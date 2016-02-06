# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-06 07:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20160204_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('PersonalEvent', 'PERSONALEVENT'), ('Holiday', 'HOLIDAY')], default='PersonalEvent', max_length=128)),
                ('event_start_datetime', models.DateTimeField(blank=True, null=True)),
                ('event_end_datetime', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_event', to='users.UserProfile')),
            ],
            options={
                'verbose_name_plural': 'Events',
                'verbose_name': 'Event',
            },
        ),
    ]
