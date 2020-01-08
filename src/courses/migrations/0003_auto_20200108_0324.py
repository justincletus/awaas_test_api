# Generated by Django 2.2.4 on 2020-01-08 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_year',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='1', help_text='Select Course year.', max_length=10),
        ),
    ]
