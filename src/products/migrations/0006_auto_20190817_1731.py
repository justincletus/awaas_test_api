# Generated by Django 2.2.4 on 2019-08-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190817_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=True, unique=True),
            preserve_default=False,
        ),
    ]
