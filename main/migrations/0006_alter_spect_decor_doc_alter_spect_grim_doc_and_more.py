# Generated by Django 4.2.16 on 2024-11-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_spect_decor_doc_alter_spect_grim_doc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spect',
            name='decor_doc',
            field=models.FileField(blank=True, default='', upload_to='materials/q/decor_doc/', verbose_name='Декорация'),
        ),
        migrations.AlterField(
            model_name='spect',
            name='grim_doc',
            field=models.FileField(blank=True, default='', upload_to='materials/q/grim_doc/', verbose_name='Грим'),
        ),
        migrations.AlterField(
            model_name='spect',
            name='kostum_doc',
            field=models.FileField(blank=True, default='', upload_to='materials/q/kostum_doc/', verbose_name='Костюм'),
        ),
        migrations.AlterField(
            model_name='spect',
            name='name',
            field=models.CharField(max_length=500, unique=True, verbose_name='Название спектакля'),
        ),
        migrations.AlterField(
            model_name='spect',
            name='rekv_doc',
            field=models.FileField(blank=True, default='', upload_to='materials/q/rekv_doc/', verbose_name='Реквизит'),
        ),
        migrations.AlterField(
            model_name='spect',
            name='svet_doc',
            field=models.FileField(blank=True, default='', upload_to='materials/q/svet_doc/', verbose_name='Свет'),
        ),
        migrations.AlterField(
            model_name='spect',
            name='video',
            field=models.FileField(blank=True, default='', upload_to='materials/q/video/', verbose_name='Видео спектакля'),
        ),
        migrations.AlterField(
            model_name='spect',
            name='video_doc',
            field=models.FileField(blank=True, default='', upload_to='materials/q/video_doc/', verbose_name='Видео'),
        ),
        migrations.AlterField(
            model_name='spect',
            name='zvuk_doc',
            field=models.FileField(blank=True, default='', upload_to='materials/q/zvuk_doc/', verbose_name='Звук'),
        ),
    ]
