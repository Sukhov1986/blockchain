# Generated by Django 5.0.6 on 2024-08-04 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0003_crypto_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crypto',
            name='price',
        ),
    ]
