
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    email=models.EmailField(verbose_name='Email Address',unique=True)

    def __str__(self):
        name = self.first_name
        return name + " {} ".format(self.last_name)


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]


 