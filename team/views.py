from django.shortcuts import render
from .models import Team

def teamView(request):
    team = Team.objects.all()
    return render(request, 'team.html', context={
        'teams': team
    })
