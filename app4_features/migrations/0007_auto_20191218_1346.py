# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-18 13:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app4_features', '0006_feature_thumbs_up'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feature',
            old_name='thumbs_up',
            new_name='thumbs_up_count',
        ),
    ]
