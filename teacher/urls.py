from django.urls import path
from . import views

urlpatterns=[
    path('',views.teacher_index_view,name="teacher"),
]