# medapp/urls.py


app_name = 'medapp'

from django.urls import path
from .views import create_appointment, upload_image, upload_report, homepage#, dashboard #register, my_login,
from . import views

app_name = 'medapp'

urlpatterns = [
    path('', homepage, name='homepage'),

    path('my_register/', views.my_register, name="my_register"),

    path('my_login/', views.my_login, name="my_login"),

    path('patient_dashboard/', views.patient_dashboard, name="patient_dashboard"),

    #path('user-logout/', views.user_logout, name="user-logout"),
    path('logout/', views.user_logout, name='logout'),
    #path('dashboard/', dashboard, name='dashboard'),

    path('create_appointment/', create_appointment, name='create_appointment'),
    path('upload_image/', upload_image, name='upload_image'),
    path('upload_report/<int:imaging_id>/', upload_report, name='upload_report'),
]
