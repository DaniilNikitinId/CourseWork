# Generated by Django 5.0.4 on 2024-04-25 07:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_remove_store_cat2'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='cat2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cats', to='store.category', verbose_name='Категории'),
        ),
    ]
