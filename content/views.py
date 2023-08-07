from django.shortcuts import render
from . models import News,Notice,Holiday,Career,About


# Create your views here.

def index_news_view(request):
    teachers=News.objects.all()
    title="News"
    template_name="content/index_news.html"
    context={"title":title,"teachers":teachers}
    return render(request,template_name,context)



def detail_news_view(request,slug):
    object=News.objects.get(slug=slug)
    objects=News.objects.all()[:4]
    template_name="content/detail_news.html"
    title="News Detail"
    context={"object":object,"objects":objects,"title":title}
    return render(request,template_name,context)

#this is where the news views end.


#this is where the notice views start.

def index_notice_view(request):
    teachers=Notice.objects.all()
    title="Notice"
    template_name="content/index_notice.html"
    context={"teachers":teachers,"title":title}
    return render(request,template_name,context)



def detail_notice_view(request,slug):
    object=Notice.objects.get(slug=slug)
    objects=Notice.objects.all()
    
    title="Notice Details"
    template_name ="content/detail_notice.html"
    context={"objects":objects,"object":object,"title":title}
    return render(request,template_name,context)


#notice view ends here

def index_holiday_view(request):
    teachers=Holiday.objects.all()
    title="Holiday"
    template_name="content/index_holiday.html"
    context={"teachers":teachers,"title":title}
    return render(request,template_name,context)



def detail_holiday_view(request,id):
    object=Holiday.objects.get(id=id)
    objects=Holiday.objects.all()
    title="Holiday Details"
    template_name="content/detail_holiday.html"
    context={"objects":objects,"object":object,"title":title}
    return render(request,template_name,context)

#holiday view ends here



def career(request):
    object =Career.objects.all()
    template_name="content/career.html"
    
    title="Career"
    context={"title":title,"object":object}
    return render(request,template_name,context)

def about(request):
    about =About.objects.all()
    title="About Us"
    template_name="content/about.html"
    context={"about":about,"title":title}
    return render(request,template_name,context)



    
    
