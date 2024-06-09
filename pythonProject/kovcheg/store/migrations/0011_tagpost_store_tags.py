# Generated by Django 5.0.4 on 2024-04-14 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_rename_category_animals_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='store.tagpost', verbose_name='тег'),
        ),
    ]
