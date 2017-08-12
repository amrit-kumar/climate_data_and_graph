# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-11 14:13
from __future__ import unicode_literals

import climate_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClimateData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('UK', 'UK'), ('England', 'England'), ('Wales\t', 'Wales'), ('Scotland', 'Scotland')], max_length=8)),
                ('max_temp', models.FileField(blank=True, null=True, upload_to=climate_app.models.get_file_path)),
                ('min_temp', models.FileField(blank=True, null=True, upload_to=climate_app.models.get_file_path)),
                ('mean_temp', models.FileField(blank=True, null=True, upload_to=climate_app.models.get_file_path)),
                ('sunshine', models.FileField(blank=True, null=True, upload_to=climate_app.models.get_file_path)),
                ('rainfall', models.FileField(blank=True, null=True, upload_to=climate_app.models.get_file_path)),
            ],
        ),
        migrations.CreateModel(
            name='ClimateStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.CharField(blank=True, max_length=999999, null=True)),
                ('Year', models.CharField(blank=True, max_length=9999, null=True)),
                ('JAN', models.CharField(blank=True, default=0, max_length=99, null=True)),
                ('FEB', models.CharField(blank=True, default=0, max_length=99, null=True)),
                ('MAR', models.CharField(blank=True, default=0, max_length=99, null=True)),
                ('APR', models.CharField(blank=True, default=0, max_length=99, null=True)),
                ('MAY', models.CharField(blank=True, default=0, max_length=99, null=True)),
                ('JUN', models.CharField(blank=True, default=0, max_length=99, null=True)),
                ('JUL', models.CharField(blank=True, default=0, max_length=99, null=True)),
                ('AUG', models.CharField(blank=True, default=0, max_length=99, null=True)),
                ('SEP', models.CharField(blank=True, default=0, max_length=99, null=True)),
                ('OCT', models.CharField(blank=True, default=0, max_length=99, null=True)),
                ('NOV', models.CharField(blank=True, default=0, max_length=99, null=True)),
                ('DEC', models.CharField(blank=True, default=0, max_length=99, null=True)),
                ('WIN', models.CharField(blank=True, default=0, max_length=99, null=True)),
                ('SPR', models.CharField(blank=True, default=0, max_length=99, null=True)),
                ('SUM', models.CharField(blank=True, default=0, max_length=99, null=True)),
                ('AUT', models.CharField(blank=True, default=0, max_length=99, null=True)),
                ('ANN', models.CharField(blank=True, default=0, max_length=99, null=True)),
            ],
        ),
    ]
