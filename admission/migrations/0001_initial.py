# Generated by Django 4.0.1 on 2022-03-11 14:01

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('student_email', models.EmailField(max_length=254, unique=True)),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE')], max_length=10)),
                ('blood_group', models.CharField(choices=[('A+', 'A RhD positive'), ('A-', 'A RhD negative'), ('B+', 'B RhD positive'), ('B', 'B RhD negative'), ('O+', 'O RhD positive'), ('O-', 'O RhD negative'), ('AB+', 'AB RhD positive'), ('AB-', 'AB RhD negative')], max_length=3)),
                ('religion', models.CharField(max_length=150)),
                ('health', models.CharField(max_length=200, verbose_name='Health Condition')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('national_id', models.CharField(max_length=100, verbose_name='National Id')),
                ('student_type', models.CharField(choices=[('Class 1', 'CLASS 1'), ('Class 2', 'CLASS 2')], max_length=10, verbose_name='Student Type')),
                ('class_type', models.CharField(choices=[('Class 1', 'CLASS 1'), ('Class 2', 'CLASS 2')], max_length=10, verbose_name='Class Type')),
                ('group_type', models.CharField(choices=[('Class 1', 'CLASS 1'), ('Class 2', 'CLASS 2')], max_length=10, verbose_name='Group Type')),
                ('second_language', models.CharField(max_length=100, verbose_name='Second Language')),
                ('father_name', models.CharField(max_length=200, verbose_name="Father's Name")),
                ('father_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name="Father's Phone")),
                ('father_education', models.CharField(max_length=200, verbose_name="Father's Education")),
                ('father_profession', models.CharField(max_length=100, verbose_name="Father's Profession")),
                ('father_designation', models.CharField(max_length=200, verbose_name="Mother's Designation")),
                ('mother_name', models.CharField(max_length=200, verbose_name="Mother's Name")),
                ('mother_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name="Mother's Phone")),
                ('mother_education', models.CharField(max_length=200, verbose_name="Mother's Education")),
                ('mother_profession', models.CharField(max_length=100, verbose_name="Mother's Profession")),
                ('mother_designation', models.CharField(max_length=100, verbose_name="Mother's Designation")),
                ('guardian', models.CharField(choices=[('Father', 'FATHER'), ('Mother', 'MOTHER'), ('Other', 'OTHER'), ('Guardian Already created', 'GUARDIAN ALREADY CREATED')], max_length=100, verbose_name='IS Guardian')),
                ('guardian_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('guardian_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('guardian_relation', models.CharField(max_length=100, verbose_name='Relationship with Guardian')),
                ('guardian_national_id', models.CharField(max_length=100, verbose_name="Guardian's National Id")),
                ('other_info', models.CharField(max_length=200)),
                ('guardian_religion', models.CharField(max_length=200)),
                ('present_address', models.TextField(blank=True, null=True, verbose_name='Present Address')),
                ('permanent_address', models.TextField(blank=True, null=True, verbose_name='Permanent Address')),
                ('previous_school', models.CharField(blank=True, max_length=100, null=True, verbose_name='Previous School')),
                ('previous_class', models.CharField(max_length=100, verbose_name='Previous class')),
            ],
        ),
    ]