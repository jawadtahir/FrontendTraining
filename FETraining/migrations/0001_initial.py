# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-09 11:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('authors', models.ManyToManyField(to='FETraining.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.IntegerField(blank=True)),
                ('carrier_code', models.IntegerField()),
                ('contact_number', models.IntegerField()),
                ('contact_method', models.CharField(choices=[('HP', 'Home Phone'), ('OP', 'Office Phone'), ('MP', 'Mobile Phone')], max_length=2)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FETraining.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(blank=True, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Dr', 'Dr'), ('Dr', 'Dr')], max_length=10)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('website', models.URLField(blank=True)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FETraining.Publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FETraining.Publisher'),
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FETraining.Name'),
        ),
    ]