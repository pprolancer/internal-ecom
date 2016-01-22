# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100, verbose_name='First Name')),
                ('middlename', models.CharField(max_length=100, verbose_name='Middle  Name')),
                ('lname', models.CharField(max_length=100, verbose_name='Last Name')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('from_person', models.ForeignKey(to='users.Parents', related_name='from_people')),
            ],
            options={
                'verbose_name_plural': 'Relationships',
                'verbose_name': 'Relationship',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100, verbose_name='First Name')),
                ('middlename', models.CharField(max_length=100, verbose_name='Middle  Name')),
                ('lname', models.CharField(max_length=100, verbose_name='Last Name')),
            ],
        ),
        migrations.AddField(
            model_name='relationship',
            name='to_person',
            field=models.ForeignKey(to='users.Student', related_name='to_people'),
        ),
    ]
