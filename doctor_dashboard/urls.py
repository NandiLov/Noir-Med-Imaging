from django.urls import path
from .views import HomeView
from . import views

app_name = 'doctor_dashboard'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

]
