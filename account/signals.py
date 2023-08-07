from django.db.models.signals import post_save
from teacher.models import Teacher
from django.conf import settings

def create_teacher(sender,instance,created,*args,**kwargs):
    pass


