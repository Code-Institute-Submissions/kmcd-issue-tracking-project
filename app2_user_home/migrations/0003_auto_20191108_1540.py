# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-08 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2_user_home', '0002_auto_20191104_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_code', models.CharField(max_length=6)),
                ('cust_name', models.CharField(max_length=50)),
                ('cust_address', models.CharField(max_length=100)),
                ('cust_city', models.CharField(max_length=30)),
                ('cust_country', models.CharField(max_length=30)),
                ('user_email_addr', models.CharField(max_length=64)),
                ('user_contact_nr', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vend_code', models.CharField(max_length=6)),
                ('vend_name', models.CharField(max_length=50)),
                ('vend_address', models.CharField(max_length=100)),
                ('vend_city', models.CharField(max_length=30)),
                ('vend_country', models.CharField(max_length=30)),
                ('vend_email_addr', models.CharField(max_length=64)),
                ('vend_contact_nr', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='vend_cust_id',
        ),
        migrations.AddField(
            model_name='userdetail',
            name='vend_cust_code',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]