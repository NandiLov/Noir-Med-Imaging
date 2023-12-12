from django.db import models

# Create your models here.
# medapp/models.py

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add fields for user profile (e.g., role: admin, doctor, patient)

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')
    date_time = models.DateTimeField()

# Define models for imaging and reports

class Imaging(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='imaging')
    image = models.ImageField(upload_to='images/')
    # Add other fields as needed

class Report(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    imaging = models.ForeignKey(Imaging, on_delete=models.CASCADE, related_name='reports')
    text = models.TextField()
