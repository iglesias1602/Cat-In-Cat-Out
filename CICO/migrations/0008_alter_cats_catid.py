# Generated by Django 4.2.5 on 2023-12-06 10:44

from django.db import migrations, models
import uuid6


class Migration(migrations.Migration):

    dependencies = [
        ('CICO', '0007_delete_cicoitem_delete_todoitem_alter_cats_ownerid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cats',
            name='catId',
            field=models.UUIDField(default=uuid6.uuid7, editable=False, primary_key=True, serialize=False),
        ),
    ]
