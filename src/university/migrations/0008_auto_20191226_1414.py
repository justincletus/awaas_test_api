# Generated by Django 2.2.4 on 2019-12-26 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0007_auto_20191226_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='universitytype',
            old_name='type',
            new_name='name',
        ),
    ]
