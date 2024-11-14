from django.contrib import admin
from .models import Home,Index

class HomeAdmin(admin.ModelAdmin):
    list_display = ('location', 'phone', 'email', 'instagram', 'facebook', 'twitter', 'linkedin')  # Ijtimoiy tarmoq URL'lari
    search_fields = ('location', 'phone', 'email')

admin.site.register(Home, HomeAdmin)

admin.site.register(Index)
