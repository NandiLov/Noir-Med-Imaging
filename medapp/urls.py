# medapp/urls.py


app_name = 'medapp'

from django.urls import path
from .views import register, dashboard, create_appointment, upload_image, upload_report, homepage


urlpatterns = [
    path('', homepage, name='homepage'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create_appointment/', create_appointment, name='create_appointment'),
    path('upload_image/', upload_image, name='upload_image'),
    path('upload_report/<int:imaging_id>/', upload_report, name='upload_report'),

]
