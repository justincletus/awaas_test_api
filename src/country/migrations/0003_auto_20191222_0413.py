# Generated by Django 2.2.4 on 2019-12-22 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0002_auto_20191222_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='state_name',
            field=models.CharField(help_text='Enter the state name', max_length=100, unique=True),
        ),
    ]
