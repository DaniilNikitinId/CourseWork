# Generated by Django 5.0.4 on 2024-04-22 12:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_brand_alter_tagpost_options_alter_store_cat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pr', models.CharField(max_length=5, null=True, verbose_name='id')),
                ('weight', models.CharField(max_length=5, null=True, verbose_name='Цена')),
                ('price', models.CharField(max_length=5, null=True, verbose_name='Вес')),
            ],
            options={
                'verbose_name': 'подкласс',
                'verbose_name_plural': 'Подклассы',
            },
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Бренд', 'verbose_name_plural': 'Бренды'},
        ),
        migrations.AddField(
            model_name='store',
            name='main_product',
            field=models.ForeignKey(help_text='Заполняется если текущий продукт является подпродуктом основного, отличаются по весу и т.п', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sub_products', to='store.product', verbose_name='Основной продукт'),
        ),
    ]
