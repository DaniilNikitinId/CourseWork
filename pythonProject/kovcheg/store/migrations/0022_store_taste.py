# Generated by Django 5.0.4 on 2024-04-23 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_store_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='taste',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Вкус'),
        ),
    ]
