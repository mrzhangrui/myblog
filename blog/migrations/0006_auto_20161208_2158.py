# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161208_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='user_name',
            field=models.CharField(max_length=50),
        ),
    ]
