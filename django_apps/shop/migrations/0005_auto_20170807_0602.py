# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 06:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20170721_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={},
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subCats', to='shop.Category'),
        ),
    ]
