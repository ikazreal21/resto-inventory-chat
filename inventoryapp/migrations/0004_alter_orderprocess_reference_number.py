# Generated by Django 3.2.11 on 2023-04-18 22:10

from django.db import migrations, models
import inventoryapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0003_alter_orderprocess_reference_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderprocess',
            name='reference_number',
            field=models.CharField(blank=True, default=inventoryapp.models.create_rand_id, editable=False, max_length=255, null=True),
        ),
    ]
