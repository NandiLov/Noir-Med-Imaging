from django.shortcuts import render , get_object_or_404
from django.views import View
from .models import Patient, UploadedDicom
from django.http import HttpResponse




def upload_dicom(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)

    if request.method == 'POST':
        for file in request.FILES.getlist('dicom_files'):
            UploadedDicom.objects.create(patient=patient, file=file)

        # Handle successful upload
        return HttpResponse("Upload successful")  # For example, returning a success message

    return render(request, 'upload_dicom.html', {'patient': patient})

def download_dicom(request, uploaded_dicom_id):
    uploaded_dicom = get_object_or_404(UploadedDicom, pk=uploaded_dicom_id)

    # Implement code to handle download
    # For example, you might serve the file for download
    # Replace the below line with your actual download logic
    return HttpResponse(f"Downloading DICOM file {uploaded_dicom_id}")




class HomeView(View):
    def get(self, request):
        return render(request, 'dashboard.html')

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




def dicom_viewer(request):
    return render(request, 'dicom_viewer.html')

