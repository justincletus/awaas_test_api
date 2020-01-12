# Generated by Django 2.2.4 on 2019-12-21 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the country name: ', max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('state_name', models.CharField(blank=True, help_text='Enter the state name: ', max_length=100, null=True)),
                ('city_name', models.CharField(blank=True, help_text='Enter the city_name name: ', max_length=100, null=True)),
                ('urban_name', models.CharField(blank=True, help_text='Enter the urban_name name: ', max_length=100, null=True)),
            ],
        ),
    ]