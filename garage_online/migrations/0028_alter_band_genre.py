# Generated by Django 4.0.4 on 2022-06-16 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage_online', '0027_remove_sociallink_band_remove_sociallink_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(18, 'rap'), (10, 'folk'), (12, 'jazz'), (15, 'pop'), (11, 'funk'), (19, 'rap - instrumental beat'), (0, 'other'), (3, 'ambient'), (2, 'alternative'), (17, 'R&B/soul'), (7, 'devotional'), (21, 'rock'), (14, 'metal'), (13, 'latin'), (8, 'electronic'), (20, 'reggae'), (4, 'blues'), (5, 'classical'), (1, 'acoustic'), (23, 'world'), (16, 'punk'), (6, 'country'), (22, 'soundtrack'), (9, 'experimental')], default=0),
        ),
    ]
