from django.db.models.signals import pre_save
from django.utils.text import slugify
from content.models import News,Notice



def create_news_details(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.title[:15])

pre_save.connect(create_news_details,sender=News)



def create_notice_detail(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.title[:5])

pre_save.connect(create_notice_detail,sender=Notice)

