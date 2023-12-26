from django.shortcuts import render, redirect, get_object_or_404
from hospital.models import Patient, Doctor, Registration

def home(request):
    return render(request, 'doctor/home.html')

def registrations(request):
    doctor_id = request.session.get('info')['id']
    doctor = Doctor.objects.filter(id=doctor_id)
    registraions = Registration.objects.filter(doctor=doctor)

    return render('doctor/registrations', {'registraions': registraions})

def medical_record(request, registration_id):
    return render('doctor/medical_record.html', {'registration_id': registration_id})
