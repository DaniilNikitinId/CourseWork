# Generated by Django 5.0.4 on 2024-05-17 09:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0038_alter_category_name_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='price',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000)], verbose_name='Цена'),
        ),
    ]
