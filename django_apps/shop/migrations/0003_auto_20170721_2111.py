# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 01:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20170721_2110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='viisible',
            new_name='visible',
        ),
    ]
