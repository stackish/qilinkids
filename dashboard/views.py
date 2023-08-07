from django.shortcuts import render
from teacher.models import *
from teacher.forms import TeacherForm
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic.edit import CreateView

from django.contrib.auth.decorators import login_required

from content.models import News,Notice

# Create your views here.
@login_required
def index_dashboard(request):
    teachers_no=Teacher.objects.all().count()
    news=News.objects.all()[:4]
    notice =Notice.objects.all()[:4]


    template_name="dashboard/homepage.html"
    context={"teachers_no":teachers_no,"news":news,"notice":notice}
    return render(request,template_name,context)

@login_required
def index_teacher_dashboard(request):
   teachers=Teacher.objects.all()
   form=TeacherForm(request.POST or None)
   
   template_name="dashboard/teacher_dashboard.html"
   context={"teachers":teachers,"form":form}
   return render(request,template_name,context)



@login_required
def generate_card(request):
    teachers=Teacher.objects.all()
    template_name="dashboard/card.html"
    context={"teachers":teachers}
    return render(request,template_name,context)