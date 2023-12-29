"""
URL configuration for hospital_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from hospital_site.views import patient, doctor, login

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", login.login),
    path("enroll/", login.enroll),
    path("logout/", login.logout),
    
    path("patient/home/", patient.home),
    path("patient/register/", patient.register),
    path("patient/register/appoint/<int:doctor_id>/", patient.register_appoint),
    path("patient/register/success/", patient.register_sucess),
    path("patient/register/appoint/", patient.register_appoint_test),
    path("patient/registrations/", patient.registrations),
    path("patient/cancel_registration/<int:registration_id>/", patient.cancel_registration),
    path("patient/personnel/", patient.personnel),
    path("patient/profile/<int:doctor_id>/", patient.profile),
    path('patient/medical_record/<int:registration_id>/', patient.medical_record),
    path('patient/personal/', patient.personal),
    path("mytest/", patient.mytest),

    path('doctor/home/', doctor.home),
    path('doctor/registrations/', doctor.registrations),
    path('doctor/medical_record/<int:registration_id>/', doctor.medical_record),
    path('doctor/accept/<int:registration_id>/', doctor.accept),
    path('doctor/finish/<int:registration_id>/', doctor.finish),
    path('doctor/medicine/', doctor.medicine),
    path('doctor/personal/', doctor.personal),
]
