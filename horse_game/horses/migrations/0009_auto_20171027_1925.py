# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0008_auto_20171027_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='expression',
            field=models.CharField(choices=[(0, 'Recessive'), (1, 'Dominant')], max_length=2),
        ),
    ]
