from django.contrib import admin
from .models import Membership,User,Event
from django.contrib.auth.admin import UserAdmin


admin.site.register(User, UserAdmin)
# Register your models here.
admin.site.register(Membership)
admin.site.register(Event)