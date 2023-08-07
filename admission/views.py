from django.shortcuts import render
from. models import Admission
from . forms import AdmissionForm


# Create your views here.
def index_admission(request):
    form =AdmissionForm(request.POST or None)
    if form.is_valid():
        form.save()
    form =AdmissionForm()

    template_name="admission/index_admission.html"
    title ="Admission"
    
    context={"title":title,"form":form}
    return render(request,template_name,context)

