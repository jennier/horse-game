# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0005_auto_20171027_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='genes',
            field=models.ManyToManyField(related_name='gene_expression', through='horses.HorseGene', to='horses.Gene'),
        ),
        migrations.AlterField(
            model_name='horsegene',
            name='gene',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genotype', to='horses.Gene'),
        ),
        migrations.AlterField(
            model_name='horsegene',
            name='horse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genotype', to='horses.Horse'),
        ),
    ]
