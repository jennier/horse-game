# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0007_auto_20171027_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horsegene',
            name='genotype',
            field=models.FloatField(max_length=2),
        ),
    ]