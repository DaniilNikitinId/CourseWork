# Generated by Django 5.0.4 on 2024-04-27 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_alter_store_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='is_published',
            field=models.BooleanField(choices=[(False, 'черновик'), (True, 'Опубликовано')], default=0, verbose_name='статус'),
        ),
    ]
