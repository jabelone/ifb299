# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0009_auto_20171023_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_admin',
            field=models.BooleanField(default='0'),
            preserve_default=False,
        ),
    ]
