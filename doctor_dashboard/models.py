

from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other patient-related fields as needed

class Appointment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    # Add other appointment-related fields as needed

class MedicalFile(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    file = models.FileField(upload_to='medical_files/', default='medical_report.txt')
    #uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_dashboard_reports' ,  default=1)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Report(models.Model):
    medical_file = models.ForeignKey(MedicalFile, on_delete=models.CASCADE)
    report_text = models.TextField()
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class DicomImage(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dicom_images/')
