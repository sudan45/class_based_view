from django import forms
from .models import *

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=['name','address','phone']


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'