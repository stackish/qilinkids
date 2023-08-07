from django.shortcuts import render
from .models import Teacher

# Create your views here.


def teacher_index_view(request):
    teachers =Teacher.objects.all()[:5]
    template_name="teacher/index.html"
    title="Teachers"
    context ={"teachers":teachers,"title":title}
    return render(request,template_name,context)
