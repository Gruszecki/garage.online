# Generated by Django 4.0.4 on 2022-06-05 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage_online', '0020_alter_band_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[(3, 'YouTube'), (6, 'Instagram'), (4, 'SoundCloud'), (1, 'Bandcamp'), (5, 'iTuens'), (2, 'Spotify'), (0, 'Facebook'), (7, 'inne')], max_length=20)),
                ('link', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(4, 'reggae'), (1, 'rock'), (6, 'muzyka elektroniczna'), (2, 'metal'), (5, 'muzyka akustyczna'), (8, 'jazz'), (3, 'pop'), (7, 'rap'), (0, 'inne')], default=0),
        ),
    ]