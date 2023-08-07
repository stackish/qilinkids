from django.db import models

# Create your models here.


class News(models.Model):
    slug=models.SlugField(blank=True,null=True)
    image=models.ImageField(upload_to="images/",blank=True,null=True)
    title =models.CharField(max_length=500)
    users=models.CharField(blank=True,null=True,max_length=100)
    date=models.DateField()

    
    description=models.TextField(blank=True,null=True)
    

    def __str__(self):
        return self.title



class Notice(models.Model):
    slug=models.SlugField(blank=True,null=True)
    title =models.CharField(max_length=500)
    uploaded_by=models.CharField(max_length=500)
    date=models.DateField()
    for_user=models.CharField(max_length=500)
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title


class Holiday(models.Model):
    title=models.CharField(max_length=500)
    start_date=models.DateField(blank=True,null=True)
    end_date=models.DateField(blank=True,null=True)


    def __str__(self):
        return self.title



class Career(models.Model):
    title_one=models.CharField(max_length=200,blank=True,null=True)
   


    def __str__(self):
        title="Avaliable Career"
        return title
    
class About(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(null=True,blank=True)
    content=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title



SITUATION=(
    ('Read','Read'),
    ('Unread','Unread'),
)

class Contact(models.Model):
    terms=models.BooleanField("Accepted the terms",default=False)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField()
    Situation=models.CharField(max_length=100,choices=SITUATION,default="Unread")

    def __str__(self):
        return self.name
