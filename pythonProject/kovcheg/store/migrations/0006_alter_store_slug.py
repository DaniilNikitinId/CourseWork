# Generated by Django 5.0.4 on 2024-04-11 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_store_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='слаг'),
        ),
    ]
