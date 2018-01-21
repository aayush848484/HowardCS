# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-29 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_classification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='classification',
            field=models.CharField(choices=[('Freshman', 'Fr'), ('Sophomore', 'Sp'), ('Junior', 'Jr'), ('Senior', 'Sr')], default='Fr', max_length=10),
        ),
    ]