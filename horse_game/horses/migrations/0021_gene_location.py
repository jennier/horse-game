# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0020_gene_gene_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='gene',
            name='location',
            field=models.CharField(default='None', max_length=10),
        ),
    ]
