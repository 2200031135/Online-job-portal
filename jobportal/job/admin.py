from django.contrib import admin
from .models import Userregistration,adminlogin,recruiterlogin
# Register your models here.

admin.site.register(Userregistration)
admin.site.register(adminlogin)
admin.site.register(recruiterlogin)
