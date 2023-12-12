# medapp/urls.py


from django.urls import path
#from . import views
from medapp.views import register, dashboard, create_appointment, upload_image, upload_report

app_name = 'medapp'

urlpatterns = [
   # path('', views.home, name='home'),
   # path('about/', views.about, name='about'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create_appointment/', create_appointment, name='create_appointment'),
    path('upload_image/', upload_image, name='upload_image'),
    path('upload_report/<int:imaging_id>/', upload_report, name='upload_report'),
    # Add more URL patterns as needed
]