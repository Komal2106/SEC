from django.contrib import admin
from django.contrib import admin
from .models import Simulation, Decision, Outcome

# Register your models here.

admin.site.register(Simulation)
admin.site.register(Decision)
admin.site.register(Outcome)
