from django.shortcuts import render
from content.models import About
from content.forms import ContactForm
from django.http import HttpResponse
import json


def base(request):
    about =About.objects.all()
    template_name="base.html"
    context={"about":about}
    return render(request,template_name,context)


def contact_view(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form=ContactForm(request.POST)
        data={}
        if form.is_valid():
            form.save()
            form=ContactForm()
            #text="Message sent Succefully"
            #messages.success(request,text)
            
            
            data['success']=True
            
            
            return HttpResponse(json.dumps(data),content_type='application/json')
        else:
            data['success']=False
            return HttpResponse(json.dumps(data),content_type='application/json') 
    else:
        form=ContactForm()
        template_name="contact.html"
        context={"form":form}
        return render(request,template_name,context)
    
