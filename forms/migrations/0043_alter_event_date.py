# Generated by Django 4.2.16 on 2024-11-08 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0042_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 8, 11, 46, 33, 604539), verbose_name='Дата мероприятия'),
        ),
    ]
