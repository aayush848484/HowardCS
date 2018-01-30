# Generated by Django 2.0.1 on 2018-01-26 20:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import event_rsvp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('title', models.CharField(help_text='The title will also be used for the event URL.', max_length=256, verbose_name='Title')),
                ('slug', models.SlugField(max_length=256, verbose_name='Slug')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Description')),
                ('start', models.DateTimeField(default='django.utils.timezone.now()', verbose_name='Start date')),
                ('end', models.DateTimeField(default=datetime.datetime(2018, 1, 27, 20, 1, 59, 561249, tzinfo=utc), verbose_name='End date')),
                ('venue', models.CharField(max_length=100, verbose_name='Venue')),
                ('street', models.CharField(blank=True, max_length=100, verbose_name='Street')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='City')),
                ('zip', models.CharField(blank=True, max_length=100, verbose_name='ZIP code')),
                ('country', models.CharField(blank=True, max_length=100, verbose_name='Country')),
                ('contact_person', models.CharField(blank=True, max_length=100, verbose_name='Contact name')),
                ('contact_email', models.EmailField(blank=True, max_length=254, verbose_name='Contact email')),
                ('contact_phone', models.CharField(blank=True, max_length=100, verbose_name='Contact phone')),
                ('available_seats', models.PositiveIntegerField(blank=True, help_text='Set this to a number if only a limited amount of slots are  available for this event. If you chose to display this on your site, you can create a sense of urgency for your users to RSVP before all slots are taken. As soon as all slots are taken, users cannot RSVP for this event any more.', null=True, verbose_name='Available seats')),
                ('hide_available_seats', models.BooleanField(default=False, help_text='If you set the number of available seats you can check this field in order to hide that number from your users.', verbose_name='Hide available seat information')),
                ('allow_anonymous_rsvp', models.BooleanField(default=False, help_text='Even anonymous users can rsvp, without adding any info.', verbose_name='Allow anonymous RSVP')),
                ('required_fields', event_rsvp.models.MultiSelectField(blank=True, choices=[('name', 'Name'), ('email', 'Email'), ('phone', 'Phone')], max_length=250, verbose_name='Required fields')),
                ('max_seats_per_guest', models.PositiveIntegerField(blank=True, help_text='Set this to a number if your guests can RSVP and declare that they are bringing some friends or family. By setting this number You can signal to the user that he or she can only bring a certain amount of additional guests.', null=True, verbose_name='Maximum amount of seats per guest')),
                ('template_name', models.CharField(blank=True, help_text='Save this event as a template to re-use it later.', max_length=100, verbose_name='Save as template')),
                ('is_published', models.BooleanField(default=False, verbose_name='is published')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Phone')),
                ('number_of_seats', models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of seats')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('is_attending', models.BooleanField(default=True, verbose_name='Attending')),
                ('message', models.TextField(blank=True, max_length=4000, verbose_name='Message')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='guests', to='event_rsvp.Event', verbose_name='Event')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]