# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-04 14:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2_user_details', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDetails',
            new_name='UserDetail',
        ),
    ]
