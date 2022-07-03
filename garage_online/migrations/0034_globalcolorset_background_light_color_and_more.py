# Generated by Django 4.0.4 on 2022-07-03 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage_online', '0033_globalcolorset'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalcolorset',
            name='background_light_color',
            field=models.CharField(default='#505050', max_length=7),
        ),
        migrations.AddField(
            model_name='globalcolorset',
            name='background_medium_color',
            field=models.CharField(default='#202020', max_length=7),
        ),
    ]
