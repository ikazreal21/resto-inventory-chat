# Generated by Django 3.2.11 on 2022-11-05 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0002_auto_20221105_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='MOP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modeofp', models.CharField(max_length=50)),
            ],
        ),
    ]
