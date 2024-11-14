from django.urls import path
from .views import serviceView

urlpatterns = [
    path('services/', serviceView, name='service')
]