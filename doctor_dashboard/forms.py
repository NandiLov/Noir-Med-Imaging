# forms.py
from django import forms
from .models import DicomImage

class DicomImageForm(forms.ModelForm):
    class Meta:
        model = DicomImage
        fields = ['image']
