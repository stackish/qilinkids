# Generated by Django 4.0.1 on 2022-03-07 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('position_class', models.CharField(max_length=200, verbose_name='Class')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('blood_group', models.CharField(choices=[('A+', 'A RhD positive'), ('A-', 'A RhD negative'), ('B+', 'B RhD positive'), ('B', 'B RhD negative'), ('O+', 'O RhD positive'), ('O-', 'O RhD negative'), ('AB+', 'AB RhD positive'), ('AB-', 'AB RhD negative')], max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
