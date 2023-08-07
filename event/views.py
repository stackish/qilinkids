from django.shortcuts import render
from .models import Event

# Create your views here.

def event_index_view(request):
    teachers=Event.objects.all()
    template_name="event/index.html"
    title="Events"
    context={"teachers":teachers,"title":title}
    return render(request,template_name,context)


def event_detail_view(request,slug):
    object=Event.objects.get(slug=slug)
    objects=Event.objects.all()[:4]
    template_name="event/detail.html"
    title="Event Details"
    context={"object":object,"title":title,"objects":objects}
    return render(request,template_name,context)
    
