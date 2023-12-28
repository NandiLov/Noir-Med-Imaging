
# Create your views here.
# medapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .forms import ImagingForm, ReportForm
from .models import Imaging
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def homepage(request):
    # Your homepage view logic here
    return render(request, 'homepage.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after successful registration
            login(request, user)
            return redirect('homepage')  # Redirect to homepage after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to homepage after login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('homepage')  # Redirect to homepage after logout









@login_required
def dashboard(request):
    return render(request, 'dashboard.html')



@login_required
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()
            return redirect('dashboard')
    else:
        form = AppointmentForm()
    return render(request, 'create_appointment.html', {'form': form})


@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImagingForm(request.POST, request.FILES)
        if form.is_valid():
            imaging = form.save(commit=False)
            imaging.patient = request.user
            imaging.save()
            return redirect('dashboard')
    else:
        form = ImagingForm()
    return render(request, 'upload_image.html', {'form': form})

@login_required
def upload_report(request, imaging_id):
    imaging = Imaging.objects.get(pk=imaging_id)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.doctor = request.user
            report.imaging = imaging
            report.save()
            return redirect('dashboard')
    else:
        form = ReportForm()
    return render(request, 'upload_report.html', {'form': form, 'imaging': imaging})


