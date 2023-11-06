# Generated by Django 4.2.6 on 2023-10-09 09:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('imdb_rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ActorMovie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_lead', models.BooleanField()),
                ('actor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.actor')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.movie')),
            ],
        ),
    ]
