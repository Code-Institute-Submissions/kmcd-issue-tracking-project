# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-07 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4_features', '0011_auto_20191231_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
