# Generated by Django 4.0.1 on 2022-03-20 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_slug_alter_event_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='image',
            new_name='images',
        ),
    ]