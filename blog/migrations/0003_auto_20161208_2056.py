# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 12:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161207_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='blog_id',
            new_name='blog_name',
        ),
    ]
