from django.shortcuts import render
from gallery.models import Gallery

# Create your views here.

def index_gallery_view(request):
    gallery = Gallery.objects.all()
    template_name="gallery/index.html"
    title="Gallery"
    context={'title':title,"gallery":gallery}
    return render(request,template_name,context)

