from django.contrib import admin
from .models import Membership,Event

# Register your models here.
admin.site.register(Membership)
admin.site.register(Event)