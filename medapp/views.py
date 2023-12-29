
# Create your views here.
# medapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .forms import ImagingForm, ReportForm, CreateUserForm, LoginForm
from .models import Imaging


from django.contrib.auth.models import auth


def homepage(request):

    return render(request, 'medapp/homepage.html')




def my_register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('medapp:patient_dashboard')  # Redirect to the 'dashboard' URL


    context = {'registerform':form}

    return render(request, 'medapp/register.html', context=context)


def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect('medapp:patient_dashboard')  # Redirect to the 'dashboard' URL

    context = {'loginform':form}

    return render(request, 'medapp/my-login.html', context=context)




def user_logout(request):
    logout(request)
    # Redirect to a specific URL after logout, or use a template for logout confirmation.
    return redirect('medapp:homepage')  # Replace 'home' with your desired URL name or path



#def user_logout(request):

 #   auth.logout(request)

  #  return redirect("medapp:homepage")



@login_required
def patient_dashboard(request):

    return render(request, 'medapp/dashboard.html')

@login_required
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()
            return redirect('patient_dashboard')
    else:
        form = AppointmentForm()
    return render(request, 'create_appointment.html', {'form': form})


@login_required(login_url="my_login")
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


