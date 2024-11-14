from django.shortcuts import render
from .models import Service

def serviceView(request):
    service = Service.objects.all()
    return render(request, 'service.html', context={
        'services': service
    })
