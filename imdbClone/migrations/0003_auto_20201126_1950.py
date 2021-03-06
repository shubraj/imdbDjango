# Generated by Django 3.1.2 on 2020-11-26 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdbClone', '0002_auto_20201126_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='torrent',
            name='casts',
            field=models.CharField(max_length=280, null=True),
        ),
        migrations.AddField(
            model_name='torrent',
            name='cover',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='torrent',
            name='directors',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='torrent',
            name='genres',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='torrent',
            name='plot',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='torrent',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='torrent',
            name='runtimes',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='torrent',
            name='title',
            field=models.CharField(max_length=2083, null=True),
        ),
        migrations.AddField(
            model_name='torrent',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
