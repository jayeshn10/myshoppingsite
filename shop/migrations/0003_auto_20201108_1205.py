# Generated by Django 3.1.2 on 2020-11-08 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_shopproduct_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopproduct',
            name='slug',
            field=models.SlugField(default='uncategorise', max_length=255),
        ),
    ]
