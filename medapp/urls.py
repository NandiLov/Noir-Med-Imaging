# medapp/urls.py


app_name = 'medapp'
from django.urls import path
from .views import register, dashboard, create_appointment, upload_image, upload_report, homepage
from . import views


from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', homepage, name='homepage'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create_appointment/', create_appointment, name='create_appointment'),
    path('upload_image/', upload_image, name='upload_image'),
    path('upload_report/<int:imaging_id>/', upload_report, name='upload_report'),
    path('download/<int:report_id>/', views.download_report, name='download_report'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
