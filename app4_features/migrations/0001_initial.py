# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-04 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_date', models.DateField(auto_now_add=True)),
                ('client_code', models.CharField(blank=True, max_length=6)),
                ('software_component', models.CharField(blank=True, max_length=25)),
                ('user_id', models.CharField(max_length=10)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('summary', models.CharField(blank=True, max_length=100)),
                ('details', models.CharField(blank=True, max_length=1000)),
                ('paid', models.IntegerField(default=5)),
                ('status', models.CharField(default='DRAFT', max_length=8)),
            ],
        ),
    ]
