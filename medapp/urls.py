# medapp/urls.py


app_name = 'medapp'

from django.urls import path
from .views import dashboard, create_appointment, upload_image, upload_report, homepage
from . import views


urlpatterns = [
    path('', homepage, name='homepage'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    #path('logout/', views.user_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create_appointment/', create_appointment, name='create_appointment'),
    path('upload_image/', upload_image, name='upload_image'),
    path('upload_report/<int:imaging_id>/', upload_report, name='upload_report'),
]
