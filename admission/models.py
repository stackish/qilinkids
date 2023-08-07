

from django.db import models
from django.contrib.auth import get_user_model
from django.forms import CharField
from phonenumber_field.modelfields import PhoneNumberField


User=get_user_model()




# Create your models here.
class Admission(models.Model):
    BLOOD_GROUP = (
        ('A+', 'A RhD positive'),
        ('A-', 'A RhD negative'),
        ('B+', 'B RhD positive'),
        ('B', 'B RhD negative'),
        ('O+', 'O RhD positive'),
        ('O-', 'O RhD negative'),
        ('AB+', 'AB RhD positive'),
        ('AB-', 'AB RhD negative'),
      
    )
    GENDER=(
        ('Male','MALE'),
        ('Female','FEMALE'),
    )
    STUDENT_TYPE=(
        ('Class 1','CLASS 1'),
        ('Class 2','CLASS 2'),
    )

    GUARDIAN =(
        ('Father','FATHER'),
        ('Mother','MOTHER'),
        ('Other','OTHER'),
        ('Guardian Already created','GUARDIAN ALREADY CREATED'),
        
        
    )
    #user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    student_email=models.EmailField(unique=True)
    date_of_birth=models.DateField(blank=True,null=True,verbose_name="Date of Birth")
    gender=models.CharField(choices=GENDER,max_length=10)
    blood_group=models.CharField(choices=BLOOD_GROUP,max_length=3)
    religion=models.CharField(max_length=150)
    health=models.CharField(verbose_name="Health Condition",max_length=200)
    phone=PhoneNumberField(blank=True)
    national_id=models.CharField(verbose_name="National Id",max_length=100)
    student_type=models.CharField(verbose_name="Student Type",choices=STUDENT_TYPE,max_length=10)
    class_type=models.CharField(verbose_name="Class Type",choices=STUDENT_TYPE,max_length=10)
    group_type=models.CharField(verbose_name="Group Type",choices=STUDENT_TYPE,max_length=10)
    second_language= models.CharField(verbose_name="Second Language",max_length=100)
    father_name=models.CharField(verbose_name="Father's Name",max_length=200)
    father_phone=PhoneNumberField(blank=True,null=True,verbose_name="Father's Phone")
    father_education=models.CharField(max_length=200,verbose_name="Father's Education")
    father_profession=models.CharField(max_length=100,verbose_name="Father's Profession")
    father_designation=models.CharField(verbose_name="Mother's Designation",max_length=200)
    mother_name=models.CharField(verbose_name="Mother's Name",max_length=200)
    mother_phone=PhoneNumberField(blank=True,null=True,verbose_name="Mother's Phone")
    mother_education=models.CharField(max_length=200,verbose_name="Mother's Education")
    mother_profession=models.CharField(max_length=100,verbose_name="Mother's Profession")
    mother_designation=models.CharField(verbose_name="Mother's Designation",max_length=100)
    guardian=models.CharField(verbose_name="IS Guardian",max_length=100,choices=GUARDIAN)
    guardian_phone=PhoneNumberField(blank=True,null=True)
    guardian_email=models.EmailField(null=True,blank=True)
    guardian_relation=models.CharField(max_length=100,verbose_name="Relationship with Guardian")
    guardian_national_id=models.CharField(verbose_name="Guardian's National Id",max_length=100)
    other_info=models.CharField(max_length=200)
    guardian_religion=models.CharField(max_length=200)
    present_address=models.TextField(verbose_name="Present Address",blank=True,null=True)
    permanent_address=models.TextField(verbose_name="Permanent Address",blank=True,null=True)
    previous_school=models.CharField(verbose_name="Previous School",blank=True,null=True,max_length=100)
    previous_class=models.CharField(verbose_name="Previous class",max_length=100)

    def __str__(self):
        return self.name


    