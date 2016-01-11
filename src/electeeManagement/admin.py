from django.contrib import admin

# Register your models here.
from .models import Electee, Social, Service_Hours, Requirements

admin.site.register(Electee)
admin.site.register(Social)
admin.site.register(Service_Hours)
admin.site.register(Requirements)