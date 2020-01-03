# Generated by Django 2.2.4 on 2019-12-21 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the university name: ', max_length=100)),
                ('country', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='country.Country')),
            ],
        ),
    ]
