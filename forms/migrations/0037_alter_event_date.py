# Generated by Django 4.2.16 on 2024-11-03 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0036_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 3, 16, 50, 1, 780881), verbose_name='Дата мероприятия'),
        ),
    ]
