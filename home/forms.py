from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

from .models import Cilt

class CiltForm(forms.ModelForm):
    class Meta:
        model = Cilt
        exclude = ['user']

        widgets = {
            'birth_place': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            }