# Generated by Django 3.2.11 on 2022-11-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailysales',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='foodinventory',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
