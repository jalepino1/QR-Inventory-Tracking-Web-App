# Generated by Django 5.0.2 on 2024-03-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0018_teacherpack_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raspberry_Pi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sa_serial_number', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
