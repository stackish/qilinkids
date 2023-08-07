from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include

from account.views import CustomLoginView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base,name="base"),
    path('Contact_us/',views.contact_view,name="contact"),
  
    path("accounts/",include("account.urls")),
    path("teacher/",include("teacher.urls")),
    path("staff/",include("staff.urls")),
    path("events/",include("event.urls")),
    path("",include("content.urls")),
    path("admission/",include("admission.urls")),
    path("gallery/",include("gallery.urls")),
    path("dashboard/",include("dashboard.urls")),
    path('accounts/login/',CustomLoginView.as_view(template_name="registration/login.html"),name="login"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


