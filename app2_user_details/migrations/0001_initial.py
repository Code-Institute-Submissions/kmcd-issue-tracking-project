# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-04 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_type', models.CharField(max_length=1)),
                ('vend_cust_id', models.IntegerField()),
                ('user_email_addr', models.CharField(max_length=64)),
                ('user_contact_nr', models.CharField(max_length=20)),
            ],
        ),
    ]
