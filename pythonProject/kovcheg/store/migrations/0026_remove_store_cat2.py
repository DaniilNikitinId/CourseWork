# Generated by Django 5.0.4 on 2024-04-24 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_store_cat2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='cat2',
        ),
    ]
