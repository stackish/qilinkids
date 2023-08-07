from django.urls import path
from . import views

urlpatterns=[
    path("",views.event_index_view,name="event"),
    path("<slug:slug>",views.event_detail_view,name="event-details"),
]

