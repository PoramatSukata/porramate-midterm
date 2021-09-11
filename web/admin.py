from django.contrib import admin
from web.models import hospital, patient, physician

# Register your models here.
admin.site.register(hospital)
admin.site.register(patient)
admin.site.register(physician)