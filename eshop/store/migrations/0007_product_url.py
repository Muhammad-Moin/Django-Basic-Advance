# Generated by Django 4.1.5 on 2023-03-05 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_customer_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]