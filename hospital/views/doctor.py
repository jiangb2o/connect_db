from django.shortcuts import render, redirect, get_object_or_404
from hospital.models import Patient, Doctor, Registration, MedicalRecord
from django import forms

def home(request):
    return render(request, 'doctor/home.html')

def registrations(request):
    doctor_id = request.session.get('info')['id']
    doctor = Doctor.objects.get(id=doctor_id)
    registrations = Registration.objects.filter(doctor=doctor)

    return render(request, 'doctor/registrations.html', {'registrations': registrations})

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        exclude = ['registration']

def medical_record(request, registration_id):
    if request.method == 'GET':
        form = MedicalRecordForm()
        return render(request, 'doctor/medical_record.html')

    registration = get_object_or_404(Registration, pk=registration_id)
    
    try:
        medical_record = MedicalRecord.objects.get(registration=registration)
    except MedicalRecord.DoesNotExist:
        medical_record = None

    form = MedicalRecordForm(request.POST, instance=medical_record)
    
    if form.is_valid():
        print('form is valid')
        medical_record = form.save(commit=False)
        medical_record.registration = registration
        medical_record.save()
        return redirect(f'/doctor/medical_record/{registration_id}')