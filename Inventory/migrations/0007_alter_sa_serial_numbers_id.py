# Generated by Django 5.0.2 on 2024-03-02 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0006_sa_serial_numbers_last_checked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sa_serial_numbers',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]