# Generated by Django 4.0.1 on 2022-03-29 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_teacher_salary_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='avatar',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
