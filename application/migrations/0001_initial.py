# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-22 02:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('register', models.CharField(max_length=10)),
                ('sap_id', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('', 'Сонгох'), ('Male', 'Male'), ('Female', 'Female')], default='Сонгох', max_length=16)),
                ('birth_day', models.DateField(default=django.utils.timezone.now)),
                ('birth_place', models.CharField(max_length=250)),
                ('driver', models.CharField(choices=[('', 'Сонгох'), ('B', 'B'), ('BC', 'B,C'), ('BCD', 'B,C,D')], default='Сонгох', max_length=16)),
                ('email', models.EmailField(max_length=100)),
            ],
            options={
                'db_table': 'general',
            },
        ),
    ]
