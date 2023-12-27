from django.shortcuts import render, redirect, get_object_or_404
from hospital.models import *
from django import forms
from django.core.paginator import Paginator

def home(request):
    return render(request, 'doctor/home.html')

def registrations(request):
    doctor_id = request.session.get('info')['id']
    doctor = Doctor.objects.get(id=doctor_id)
    registrations = Registration.objects.filter(doctor=doctor)


    # 分页
    paginator = Paginator(registrations, 5)
    page_number = request.GET.get('page')
    registrations = paginator.get_page(page_number)

    return render(request, 'doctor/registrations.html', {'registrations': registrations})

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        exclude = ['registration']

def medical_record(request, registration_id):
    registration = get_object_or_404(Registration, pk=registration_id)
    
    try:
        medical_record = MedicalRecord.objects.get(registration=registration)
    except MedicalRecord.DoesNotExist:
        medical_record = None

    patient = registration.patient

    if request.method == 'GET':
        if medical_record == None:
            form = None
        else:
            form = MedicalRecordForm(instance=medical_record)
        return render(request, 'doctor/medical_record.html', {'form': form, 'patient': patient})

    form = MedicalRecordForm(request.POST, instance=medical_record)
    if form.is_valid():
        medical_record = form.save(commit=False)
        medical_record.registration = registration
        medical_record.save()
    return render(request, 'doctor/medical_record.html', {'form': form, 'patient': patient})
    
def accept(request, registration_id):
    registration = get_object_or_404(Registration, pk=registration_id)
    registration.status = 2
    registration.save()
    print('accept', registration_id)
    return redirect('/doctor/registrations')

def finish(request, registration_id):
    registration = get_object_or_404(Registration, pk=registration_id)
    registration.status = 3
    registration.save()
    return redirect('/doctor/registrations')