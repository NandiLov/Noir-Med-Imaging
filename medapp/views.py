
# Create your views here.
# medapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .forms import ImagingForm, ReportForm, CreateUserForm, LoginForm
from .models import Imaging, User, Report
from zipfile import ZipFile
import os
from django.conf import settings
from django.contrib.auth.models import auth
from django.contrib.auth.models import Group

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from mimetypes import guess_type




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
            return redirect("medapp:patient_dashboard")
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
            uploaded_file = request.FILES['image_or_zip']

            if uploaded_file.name.endswith('.zip'):
                # Handle a zip file upload
                with ZipFile(uploaded_file, 'r') as zip_ref:
                    extracted_folder = os.path.splitext(uploaded_file.name)[0]  # Extract folder name
                    extracted_path = os.path.join(settings.MEDIA_ROOT, 'images_or_zips', extracted_folder)  # Define extraction path within MEDIA_ROOT
                    os.makedirs(extracted_path, exist_ok=True)  # Create folder if it doesn't exist
                    zip_ref.extractall(extracted_path)  # Extract contents of the zip file

                # Save the path to the extracted folder in the model
                imaging.image_or_zip = os.path.join('images_or_zips', extracted_folder)
            else:
                # Handle a single image upload
                imaging.image_or_zip = uploaded_file

            imaging.save()
            return redirect('medapp:upload_successful')
    else:
        form = ImagingForm()
    return render(request, 'upload_image.html', {'form': form})

@login_required
def upload_successful(request):
    return render(request, 'medapp/upload_successfull.html')


def download_file(request, file_path):
    absolute_file_path = os.path.join(settings.MEDIA_ROOT, file_path)

    if os.path.exists(absolute_file_path) and not os.path.isdir(absolute_file_path):
        file_extension = os.path.splitext(absolute_file_path)[1].lower()

        with open(absolute_file_path, 'rb') as file:
            content_type, _ = guess_type(absolute_file_path)
            response = HttpResponse(file.read(), content_type=content_type)

            # Set the content disposition based on file type
            if file_extension in ['.zip']:
                response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(absolute_file_path)
            elif file_extension in ['.jpg', '.jpeg', '.png', '.gif']:
                response['Content-Disposition'] = 'inline; filename=%s' % os.path.basename(absolute_file_path)

            return response
    else:
        return HttpResponse("File not found", status=404)






def patients_list(request):
    patients_group = Group.objects.get(name='patients')
    patients = patients_group.user_set.all()
    return render(request, 'patients_list.html', {'patients': patients})

def patient_details(request, username):
    patient = get_object_or_404(User, username=username)
    imaging_files = Imaging.objects.filter(patient=patient)
    reports = Report.objects.filter(imaging__in=imaging_files)
    return render(request, 'patient_details.html', {'patient': patient, 'imaging_files': imaging_files, 'reports': reports})#'report': report







def write_report(request, imaging_id):
    imaging = get_object_or_404(Imaging, pk=imaging_id)
    if request.method == 'POST':
        # Process report form submission
        # Save the report details associated with the imaging
        return redirect('medapp:patient_details', username=imaging.patient.username)
    else:
        return render(request, 'write_report.html', {'imaging': imaging})

def upload_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.save()
            return redirect(request, 'medapp/upload_successfull.html')  # Redirect to a success view after upload
    else:
        form = ReportForm()
    return render(request, 'upload_report_byname.html', {'form': form})


def download_report(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    # Here, you may want to add additional logic for permissions,
    # ensuring the user has access to this report, etc.
    # For now, let's assume anyone who has the link can download the report.
    file_url = report.get_report_file_url()
    # Implement logic to handle the file download (e.g., using Django's FileResponse)
    response = HttpResponse(content_type='application/pdf')  # Adjust content_type as needed
    response['Content-Disposition'] = f'attachment; filename="{report.report_file.name}"'
    response['X-Sendfile'] = file_url  # Use appropriate method for file serving in your setup
    return response





