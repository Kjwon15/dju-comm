# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrating', '0003_auto_20170821_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='category',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='class',
            name='classification',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='class',
            name='department',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='class',
            name='major',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='class',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='class',
            name='university',
            field=models.CharField(max_length=40),
        ),
    ]
