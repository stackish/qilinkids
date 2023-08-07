from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


User = settings.AUTH_USER_MODEL

# Create your models here.
class Teacher(models.Model):
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
        ('Female','FEMALE')
    )
    ROLE=(
        ('TEACHER','TEACHER'),
    )

    SG=(
        ('Teacher Grade','Teacher Grade'),
    )

    ST=(
        ('hourly','Hourly'),
        ('weekly','Weekly'),
        ('Monthly','Monthly'),
    )
    avatar= models.ImageField(upload_to="images/",blank=False,null=False)
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    position_class = models.CharField(verbose_name="Responsibility",max_length=200)
    country = CountryField(blank_label='(Select Country)')
    phone=PhoneNumberField(blank=True)
    National_id=models.IntegerField(blank=True,null=True)
    gender=models.CharField(max_length=6,choices=GENDER,null=True,blank=True)
    blood_group =models.CharField(max_length=3,choices=BLOOD_GROUP,null=True,blank=True)
    religion=models.CharField(max_length=200,null=True,blank=True)
    date_of_birth=models.DateField()
    present_address=models.CharField(max_length=400,blank=True,null=True)
    permanent_address=models.CharField(max_length=400,blank=True,null=True)
    role=models.CharField(max_length=20,choices=ROLE,null=True,blank=True)
    salary_grade=models.CharField(max_length=20,choices=SG,null=True,blank=True)
    salary_type=models.CharField(max_length=20,choices=ST,null=True,blank=True)


    def __str__(self):
        return str(self.user)