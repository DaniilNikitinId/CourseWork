# Generated by Django 5.0.4 on 2024-05-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_remove_store_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='tagsCats',
            field=models.ManyToManyField(blank=True, related_name='tagsCats', to='store.tagpost', verbose_name='тег для кошек'),
        ),
    ]
