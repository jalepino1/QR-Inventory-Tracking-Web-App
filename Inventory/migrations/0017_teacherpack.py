# Generated by Django 5.0.2 on 2024-03-18 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0016_delete_teacherpack_delete_teacherpack_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacherpack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('serial_number', models.CharField(max_length=100)),
                ('sa_serial_number', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
