# Generated by Django 5.0.4 on 2024-04-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_remove_store_main_product_store_main_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='is_published',
            field=models.BooleanField(choices=[(False, 'черновик'), (True, 'Опубликовано'), (True, 'Подтовар')], default=0, verbose_name='статус'),
        ),
    ]
