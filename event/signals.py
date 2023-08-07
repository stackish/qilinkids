from django.db.models.signals import pre_save
from django.utils.text import slugify
from event.models import Event



def create_event_details(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.title[:15])

pre_save.connect(create_event_details,sender=Event)
