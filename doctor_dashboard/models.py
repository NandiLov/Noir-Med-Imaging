

from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    name = models.CharField(max_length=100)
    # Add other patient details

class UploadedDicom(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    file = models.FileField(upload_to='dicom_uploads/')  # Folder or multiple files





class Appointment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    # Add other appointment-related fields as needed

class MedicalFile(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    file = models.FileField(upload_to='medical_files/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Report(models.Model):
    medical_file = models.ForeignKey(MedicalFile, on_delete=models.CASCADE)
    report_text = models.TextField()
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class DicomImage(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dicom_images/')
