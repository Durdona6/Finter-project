from django.urls import path
from .views import aboutView

urlpatterns = [
    path('about/', aboutView, name='about')
]