from django.urls import path
from . import views


urlpatterns= [
    path('',views.index_dashboard,name="dashboard"),
    path('teacher/',views.index_teacher_dashboard,name="teacher_dashboard"),
    path('generate-card/',views.generate_card,name="card-generate"),




]