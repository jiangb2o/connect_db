from django.contrib import admin
from hospital import models

admin.site.register(models.Patient)
admin.site.register(models.Doctor)
admin.site.register(models.Department)
admin.site.register(models.Registration)