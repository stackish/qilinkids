# Generated by Django 4.0.1 on 2022-03-11 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_notice_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='title_five',
        ),
        migrations.RemoveField(
            model_name='career',
            name='title_four',
        ),
        migrations.RemoveField(
            model_name='career',
            name='title_seven',
        ),
        migrations.RemoveField(
            model_name='career',
            name='title_six',
        ),
        migrations.RemoveField(
            model_name='career',
            name='title_three',
        ),
        migrations.RemoveField(
            model_name='career',
            name='title_two',
        ),
    ]
