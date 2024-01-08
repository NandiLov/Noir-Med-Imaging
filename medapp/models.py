from django.db import models

# Create your models here.
# medapp/models.py

from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional fields for user profile
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')  # Provide a default value

    def __str__(self):
        return f"{self.user.username}'s Profile"

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User  # Reference the User model correctly
        fields = ['username', 'email', 'password1', 'password2']

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')
    date_time = models.DateTimeField()




class Imaging(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='imaging')
    image_or_zip = models.FileField(upload_to='images_or_zips/')
    # Add other fields as needed



class Report(models.Model):
    patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reports')
    imaging = models.ForeignKey(Imaging, on_delete=models.CASCADE, related_name='reports')
    text = models.TextField()
    #report_file = models.FileField(upload_to='reports/', default='default_report.pdf')
    file = models.FileField(upload_to='reports/',default='default_file.pdf')

    def get_report_file_url(self):
        return self.report_file.url
