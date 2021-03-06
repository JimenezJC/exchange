# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 22:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20170809_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='nut.jpg', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='nut.jpg', upload_to='', verbose_name='upload image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(default='Nut', max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='lastActive',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(db_index=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='shop.Item'),
        ),
    ]
