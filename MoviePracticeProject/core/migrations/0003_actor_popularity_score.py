# Generated by Django 4.2.6 on 2023-10-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_release_date_movie_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='popularity_score',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
    ]
