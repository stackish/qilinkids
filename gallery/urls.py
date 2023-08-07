from django.urls import path
from . import views

urlpatterns = [
    path("",views.index_gallery_view,name="gallery"),
]
