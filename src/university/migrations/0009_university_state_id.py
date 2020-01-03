# Generated by Django 2.2.4 on 2019-12-26 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0005_auto_20191223_0525'),
        ('university', '0008_auto_20191226_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='state_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='country.State'),
        ),
    ]
