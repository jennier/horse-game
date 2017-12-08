# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0018_auto_20171029_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]