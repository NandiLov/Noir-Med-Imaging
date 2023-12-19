from django.urls import path
from .views import HomeView, PatientsView, PatientDetailView, UploadReportView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('patients/', PatientsView.as_view(), name='patients'),
    path('patients/<int:patient_id>/', PatientDetailView.as_view(), name='patient_detail'),
    path('upload_report/<int:file_id>/', UploadReportView.as_view(), name='upload_report'),
]
