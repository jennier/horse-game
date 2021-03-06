# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0002_auto_20171027_0306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('symbol', models.CharField(max_length=4)),
                ('expression', models.CharField(choices=[(0, 'Recessive'), (1, 'Dominant')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='HorseGene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genotype', models.IntegerField()),
                ('gene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gene_expression', to='horses.Gene')),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gene_expression', to='horses.Horse')),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('stat_type', models.CharField(choices=[(0, 'Fixed'), (1, 'Flexible')], max_length=1)),
                ('hidden', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='horse',
            name='genes',
            field=models.ManyToManyField(related_name='genotype', through='horses.HorseGene', to='horses.Gene'),
        ),
    ]
