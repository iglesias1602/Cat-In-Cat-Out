# Generated by Django 4.2.5 on 2023-10-04 06:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CICO', '0005_rename_time_tablestatus_heure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablestatus',
            name='heure',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
