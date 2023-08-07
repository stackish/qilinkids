from django.shortcuts import render
from .models import Staff

# Create your views here.
def staff_index_view(request):
    teachers=Staff.objects.all()[:5]
    template_name="staff/index.html"
    title="Staffs"
    context={"teachers":teachers,"title":title}
    return render(request,template_name,context)