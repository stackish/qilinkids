# Generated by Django 4.0.1 on 2022-03-28 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_teacher_date_of_birth_teacher_permanent_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='role',
            field=models.CharField(blank=True, choices=[('TEACHER', 'TEACHER')], max_length=20, null=True),
        ),
    ]
