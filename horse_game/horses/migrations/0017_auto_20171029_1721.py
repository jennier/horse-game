# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0016_breed_genes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]