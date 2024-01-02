from django.urls import path
from .views import HomeView, PatientsView, PatientDetailView, UploadReportView
from . import views



urlpatterns = [
    path('patient/<int:patient_id>/upload_dicom/', views.upload_dicom, name='upload_dicom'),
    path('dicom/<int:uploaded_dicom_id>/download/', views.download_dicom, name='download_dicom'),
    # Add other URLs as needed
]





urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('patients/', PatientsView.as_view(), name='patients'),
    path('patients/<int:patient_id>/', PatientDetailView.as_view(), name='patient_detail'),

    path('patient/<int:patient_id>/upload_dicom/', views.upload_dicom, name='upload_dicom'),
    path('dicom/<int:uploaded_dicom_id>/download/', views.download_dicom, name='download_dicom'),

    path('upload_report/<int:file_id>/', UploadReportView.as_view(), name='upload_report'),
    path('dicom-viewer/', views.dicom_viewer, name='dicom_viewer'),
]
