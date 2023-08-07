from django.db import models

# Create your models here.


class Event(models.Model):
    slug=models.SlugField(blank=True,null=True)
    images=models.ImageField(upload_to="images/",blank=True,null=True)
    title =models.CharField(verbose_name="Position",max_length=500)
    users=models.CharField(blank=True,null=True,max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()
    location=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    

    def __str__(self):
        return self.title

