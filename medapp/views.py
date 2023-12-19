
# Create your views here.
# medapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .forms import ImagingForm, ReportForm
from .models import Imaging



def homepage(request):
    return render(request, 'homepage.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

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


