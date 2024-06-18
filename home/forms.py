from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

from .models import Vehicle, VehicleType

class VehicleForm(forms.ModelForm):

    type = forms.ModelChoiceField(queryset=VehicleType.objects.all(), empty_label="Vehicle Type")

    class Meta:
        model = Vehicle
        fields = ['type', 'number']