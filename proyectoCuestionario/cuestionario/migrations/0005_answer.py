# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-31 15:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuestionario', '0004_auto_20180131_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_A', models.IntegerField()),
                ('option_B', models.IntegerField()),
                ('option_C', models.IntegerField()),
                ('option_D', models.IntegerField()),
                ('questionary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionary', to='cuestionario.Questionary')),
            ],
        ),
    ]
