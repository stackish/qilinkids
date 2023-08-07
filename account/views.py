from django.http import HttpResponseRedirect
from django.shortcuts import render,reverse
from django.contrib.auth.views import LoginView

from account.forms import LoginForm

# Create your views here.
class CustomLoginView(LoginView):
    form_class=LoginForm
    templaate_name="registration/login.html"
    success_url ='base'
    



    def dispatch(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('base'))
        return super(CustomLoginView,self).dispatch(*args,**kwargs)

