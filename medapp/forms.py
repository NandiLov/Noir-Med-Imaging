# forms

from django import forms
from .models import Appointment
from .models import Imaging, Report

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date_time']

class ImagingForm(forms.ModelForm):
    class Meta:
        model = Imaging
        fields = ['image']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['text']
