# Generated by Django 4.2.6 on 2023-10-10 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_actor_options_alter_actor_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'ordering': ['age']},
        ),
    ]
