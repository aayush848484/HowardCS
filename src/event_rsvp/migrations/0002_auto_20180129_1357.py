# Generated by Django 2.0.1 on 2018-01-29 18:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event_rsvp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 30, 18, 57, 12, 599143, tzinfo=utc), verbose_name='End date'),
        ),
    ]
