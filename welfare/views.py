from django.shortcuts import render
from django.views import View


class CreditView(View):
    def get(self, request):
        return render(request, 'welfare/credit.html', {})


class SchoolView(View):
    def get(self, request):
        return render(request, 'welfare/school.html', {})


class ClinicView(View):
    def get(self, request):
        return render(request, 'welfare/clinic.html', {})
