# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0004_auto_20171027_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='genes',
            field=models.ManyToManyField(related_name='genotype', through='horses.HorseGene', to='horses.Gene'),
        ),
    ]
