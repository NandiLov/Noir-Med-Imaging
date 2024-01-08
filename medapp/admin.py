
from django.contrib import admin
from .models import Appointment, Imaging, Report, UserProfile  # Import your models

admin.site.register(Appointment)
admin.site.register(Imaging)
admin.site.register(Report)
admin.site.register(UserProfile)
