from django.shortcuts import render , redirect
from django.views import View
from .forms import DicomImageForm

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


def upload_dicom(request):
    if request.method == 'POST':
        form = DicomImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Specify the URL to redirect after successful upload
    else:
        form = DicomImageForm()

    return render(request, 'upload_dicom.html', {'form': form})

def dicom_viewer(request):
    return render(request, 'dicom_viewer.html')

