# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0017_auto_20171029_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='breed',
            name='height_max',
            field=models.IntegerField(default=17),
        ),
        migrations.AddField(
            model_name='breed',
            name='height_min',
            field=models.IntegerField(default=13),
        ),
        migrations.AlterField(
            model_name='horse',
            name='height',
            field=models.IntegerField(default=15),
        ),
    ]
