# Generated by Django 4.0.4 on 2022-05-30 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage_online', '0005_alter_band_country_alter_band_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(1, 'rock'), (2, 'metal'), (6, 'muzyka elektroniczna'), (3, 'pop'), (7, 'rap'), (4, 'reggae'), (5, 'muzyka akustyczna'), (0, 'inne'), (8, 'jazz')], default=0),
        ),
    ]
