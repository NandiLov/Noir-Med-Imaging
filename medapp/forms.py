# forms

from django import forms
from .models import Appointment
from .models import Imaging, Report
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput



# - Create/Register a user (Model Form)

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


# - Authenticate a user (Model Form)

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date_time']


class ImagingForm(forms.ModelForm):
    class Meta:
        model = Imaging
        fields = ['image_or_zip']


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['text']


