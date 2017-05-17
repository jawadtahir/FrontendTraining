# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-12 13:59
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('FETraining', '0006_auto_20170511_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to='FETraining.Name'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to='FETraining.Name'),
        ),
    ]
