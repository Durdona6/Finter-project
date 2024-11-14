from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# CustomUser modelini admin panelga qo‘shamiz
admin.site.register(CustomUser, UserAdmin)
