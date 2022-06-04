# Generated by Django 4.0.4 on 2022-06-04 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage_online', '0017_alter_band_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(5, 'muzyka akustyczna'), (8, 'jazz'), (6, 'muzyka elektroniczna'), (7, 'rap'), (4, 'reggae'), (2, 'metal'), (0, 'inne'), (3, 'pop'), (1, 'rock')], default=0),
        ),
    ]