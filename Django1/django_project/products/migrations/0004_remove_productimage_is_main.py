# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-04-13 09:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productimage_is_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='is_main',
        ),
    ]