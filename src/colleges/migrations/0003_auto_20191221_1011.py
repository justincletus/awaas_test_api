# Generated by Django 2.2.4 on 2019-12-21 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0002_auto_20191221_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='university_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='university.University'),
        ),
    ]
