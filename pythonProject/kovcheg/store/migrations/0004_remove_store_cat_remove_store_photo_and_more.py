# Generated by Django 5.0.4 on 2024-04-11 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_store_tags_delete_tagpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='store',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='store',
            name='slug',
        ),
    ]
