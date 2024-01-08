from django.shortcuts import render
from django.views import View







class HomeView(View):
    def get(self, request):
        return render(request, 'dashboard.html')


def dashboard(request):

    return render(request, 'doctor_dashboard/dashboard.html')

