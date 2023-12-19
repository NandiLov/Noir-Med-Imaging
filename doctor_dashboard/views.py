from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class PatientsView(View):
    def get(self, request):
        patients = []  # Fetch patients from the database or any source
        return render(request, 'patients.html', {'patients': patients})

class PatientDetailView(View):
    def get(self, request, patient_id):
        # Fetch patient details from the database or any source
        patient = {}  # Replace with actual patient details
        return render(request, 'patient_detail.html', {'patient': patient})

class UploadReportView(View):
    def get(self, request, file_id):
        # Fetch medical file details from the database or any source
        medical_file = {}  # Replace with actual medical file details
        return render(request, 'upload_report.html', {'medical_file': medical_file})
