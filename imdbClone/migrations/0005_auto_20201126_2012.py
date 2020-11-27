# Generated by Django 3.1.2 on 2020-11-26 20:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('imdbClone', '0004_torrent_added_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torrent',
            name='added_on',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
