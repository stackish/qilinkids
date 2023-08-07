
from django.db import models

# Create your models here.
class Gallery(models.Model):
    image=models.ImageField(upload_to="images/")

    def __str__(self):
        display="Carosuel {}".format(self.id)
        return display