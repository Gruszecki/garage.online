# Generated by Django 4.0.4 on 2022-07-05 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage_online', '0036_alter_band_image_alter_song_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
