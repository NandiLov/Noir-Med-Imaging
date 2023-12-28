# forms

from django import forms
from .models import Appointment
from .models import Imaging, Report
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


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
