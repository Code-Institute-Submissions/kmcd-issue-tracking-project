# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-04 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3_issue_logging', '0014_auto_20191202_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='progress',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
