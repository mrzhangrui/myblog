# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-12 12:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20161208_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='comment',
        ),
    ]