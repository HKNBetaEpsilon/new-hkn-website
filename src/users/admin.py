from django.contrib import admin

# Register your models here.
from .models import Member
from .models import Electee
from .models import Social
from .models import Service_Hours

admin.site.register(Member)
admin.site.register(Electee)
admin.site.register(Social)
admin.site.register(Service_Hours)