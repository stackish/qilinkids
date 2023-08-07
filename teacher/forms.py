from django import forms


from django import forms
from django.forms import ModelForm
from .models import Teacher

class TeacherForm(ModelForm):
    class Meta:
        model=Teacher
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'placeholder': 'Phone Number'})
       # self.fields['comment'].widget.attrs.update(size='40')