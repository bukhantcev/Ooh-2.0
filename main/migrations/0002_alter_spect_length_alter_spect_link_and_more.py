# Generated by Django 4.2.16 on 2024-11-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spect',
            name='length',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Длительность спектакля'),
        ),
        migrations.AlterField(
            model_name='spect',
            name='link',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='Ссылка на спектакль'),
        ),
        migrations.AlterField(
            model_name='spect',
            name='video',
            field=models.FileField(blank=True, default='', upload_to='materials/<built-in function id>/video/', verbose_name='Видео спектакля'),
        ),
    ]
