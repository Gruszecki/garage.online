# Generated by Django 4.0.4 on 2022-06-29 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage_online', '0029_song_main_song_alter_band_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='image',
            field=models.ImageField(upload_to='media/bands_photos'),
        ),
    ]