# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 17:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0008_auto_20171023_1732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='long_descriptiion',
            new_name='long_description',
        ),
    ]