from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'select_service', 'email', 'message')  # Ko'rsatiladigan maydonlar
    search_fields = ('full_name', 'phone_number', 'email')  # Qidiruv maydonlari
    list_filter = ('select_service',)  # Filtrlash maydonlari

admin.site.register(Contact, ContactAdmin)
