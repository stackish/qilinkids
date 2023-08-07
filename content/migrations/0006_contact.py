# Generated by Django 4.0.1 on 2022-05-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_about_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms', models.BooleanField(default=False, verbose_name='Accepted the terms')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('Situation', models.CharField(choices=[('Read', 'Read'), ('Unread', 'Unread')], default='Unread', max_length=100)),
            ],
        ),
    ]