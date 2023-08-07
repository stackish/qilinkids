
from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


User = settings.AUTH_USER_MODEL

# Create your models here.
class Staff(models.Model):
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
    avatar= models.ImageField(upload_to="images/",blank=True,null=True)
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    position_class = models.CharField(verbose_name="Class",max_length=200)
    country = CountryField(blank_label='(select country)')
    #phone=PhoneNumberField(blank=True)
    blood_group =models.CharField(max_length=3,choices=BLOOD_GROUP)


    def __str__(self):
        staff=str(self.user)
        return staff + "---->  {} ".format(self.position_class)