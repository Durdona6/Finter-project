from django.urls import path
from .views import teamView

urlpatterns = [
    path('team/', teamView, name='team')
]