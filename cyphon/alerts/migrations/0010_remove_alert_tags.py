# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 20:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0009_auto_20170810_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='tags',
        ),
    ]
