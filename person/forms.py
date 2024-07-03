from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['birth_place', 'birth_date']
    
        widgets = {
            'birth_place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Birth Place'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'text'}),
        }
