# Generated by Django 4.2.16 on 2024-11-03 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0035_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 3, 12, 59, 37, 797352), verbose_name='Дата мероприятия'),
        ),
    ]
