# Generated by Django 4.1 on 2022-10-03 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]