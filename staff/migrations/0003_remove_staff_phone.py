# Generated by Django 4.0.1 on 2022-03-20 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_rename_teacher_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='phone',
        ),
    ]
