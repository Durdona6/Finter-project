from django.shortcuts import render
from .models import About

def aboutView(request):
    about = About.objects.all()
    context = {
        'abouts': about
    }
    return render(request, 'about.html', context)
