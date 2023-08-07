from django.forms import ModelForm
from . models import Admission



class AdmissionForm(ModelForm):
    class Meta:
        model=Admission
        fields="__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    


