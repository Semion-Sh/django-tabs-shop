# Generated by Django 4.1 on 2022-10-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabs', '0010_remove_songs_piano_tabs_delete_piano_tabs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guitar_tabs',
            name='price',
        ),
        migrations.AddField(
            model_name='songs',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]